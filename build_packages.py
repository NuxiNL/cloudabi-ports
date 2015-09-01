#!/usr/bin/env python3

import hashlib
import os
import random
import shutil
import stat
import subprocess
import sys

ARCHITECTURES = ['x86_64']

DIR_BUILD = os.path.join(os.getcwd(), '_obj/build')
DIR_DISTFILES = os.path.join(os.getcwd(), '_obj/distfiles')
DIR_INSTALL = os.path.join(os.getcwd(), '_obj/install')
DIR_REPOSITORY = os.path.join(os.getcwd(), 'packages')
DIR_SOURCES = os.path.join(os.getcwd(), '_obj/srcs')

PACKAGES = {}
PACKAGES_BUILT = set()
PACKAGES_BUILDING = set()

def build_nothing(ctx):
  pass

def package(**kwargs):
  name = kwargs['name']
  if name in PACKAGES:
    raise Exception('%s listed multiple times' % name)
  if 'build_cmd' not in kwargs:
    kwargs['build_cmd'] = build_nothing
  if 'distfiles' not in kwargs:
    kwargs['distfiles'] = ['%s-%s.tar' % (kwargs['name'], kwargs['version'])]
  if 'lib_depends' not in kwargs:
    kwargs['lib_depends'] = set()
  PACKAGES[name] = kwargs

DISTFILES = {}

def distfile(**kwargs):
  name = kwargs['name']
  if name in DISTFILES:
    raise Exception('%s listed multiple times' % name)
  DISTFILES[name] = kwargs

# Parse all of the BUILD rules.
for root, dirs, files in os.walk(DIR_REPOSITORY):
  if 'BUILD' in files:
    with open(os.path.join(root, 'BUILD'), 'r') as f:
      exec(f.read())

def get_distfile(distname):
  # Fetch distfile.
  distfile = os.path.join(DIR_DISTFILES, distname)
  site = random.sample(DISTFILES[distname]['master_sites'], 1)[0]
  if not os.path.isfile(distfile):
    subprocess.check_call(['fetch', '-o', distfile, site + distname])
  # Validate checksum.
  with open(distfile, 'rb') as f:
    if DISTFILES[distname]['checksum'] != hashlib.sha256(f.read()).hexdigest():
      raise Exception('Checksum mismatch')
  return distfile

def get_extracted(distname):
  # Extract distfile.
  source_directory = os.path.join(DIR_SOURCES, distname)
  if not os.path.isdir(source_directory):
    os.makedirs(source_directory)
    subprocess.check_call(['tar', '-xC', source_directory, '-f',
                           get_distfile(distname)])

  # Remove leading directory names.
  while True:
    entries = os.listdir(source_directory)
    if len(entries) != 1:
      break
    new_directory = os.path.join(source_directory, entries[0])
    if not os.path.isdir(new_directory):
      break
    source_directory = new_directory
  return source_directory

def get_patched(distname):
  source_directory = get_extracted(distname)
  dot_patched = os.path.join(source_directory, '.patched')
  if 'patches' in DISTFILES[distname] and not os.path.isfile(dot_patched):
    for patch in DISTFILES[distname]['patches']:
      with open(os.path.join(DIR_REPOSITORY, patch)) as f:
        subprocess.check_call(['patch', '-d', source_directory, '-sp0'],
                              stdin=f)
    open(dot_patched, 'w').close()
  return source_directory

def copy_file(source, target, preserve_metadata):
  if os.path.exists(target):
    raise Exception('About to overwrite %s with %s' % (target, source))
  try:
    os.makedirs(os.path.dirname(target))
  except:
    pass
  shutil.copy(source, target)
  if preserve_metadata:
    shutil.copystat(source, target)

def copy_file_or_tree(source, target, preserve_metadata):
  if os.path.isdir(source):
    for root, dirs, files in os.walk(source):
      for f in files:
        source_filename = os.path.join(root, f)
        target_filename = os.path.normpath(
            os.path.join(target, os.path.relpath(source_filename, source)))
        copy_file(source_filename, target_filename, preserve_metadata)
  else:
    copy_file(source, target, preserve_metadata)

def get_recursive_includes(pkg):
  includes = set()
  for dep in pkg['lib_depends']:
    includes.add('-I' + os.path.join(DIR_INSTALL, dep, 'include'))
    includes = includes.union(get_recursive_includes(PACKAGES[dep]))
  return includes

class PackageBuilder:
  def __init__(self, pkg, build_directory, install_directory):
    self._pkg = pkg
    self._build_directory = build_directory
    self._install_directory = install_directory
    self._library_number = 0

    self._env_ar = '/usr/local/bin/x86_64-unknown-cloudabi-ar'
    self._env_cc = '/usr/local/bin/x86_64-unknown-cloudabi-cc'
    self._env_cxx = '/usr/local/bin/x86_64-unknown-cloudabi-c++'
    self._env_cflags = (['-nostdinc', '-O2', '-g', '-fstack-protector-strong'] +
                        sorted(get_recursive_includes(self._pkg)))
    self._env_cxxflags = self._env_cflags + ['-nostdlibinc', '-nostdinc++']
    self._env_vars = [
        'AR=' + self._env_ar,
        'CC=' + self._env_cc,
        'CXX=' + self._env_cxx,
        'CFLAGS=' + ' '.join(self._env_cflags),
        'CXXFLAGS=' + ' '.join(self._env_cxxflags),
        'LDFLAGS=-nostdlib',
        'PATH=/bin:/sbin:/usr/bin:/usr/sbin',
    ]

  def _full_path(self, path):
    return os.path.join(self._build_directory, path)


  def compile(self, source_file, cflags=[]):
    ext = os.path.splitext(source_file)[1]
    output = source_file + '.o'
    if ext == '.c':
      print('CC', source_file)
      self.run_command(
          '.',
          [self._env_cc] + self._env_cflags + cflags +
          ['-c', '-o', self._full_path(output), self._full_path(source_file)])
    elif ext == '.cpp':
      print('CXX', source_file)
      self.run_command(
          '.',
          [self._env_cxx] + self._env_cxxflags + cflags +
          ['-c', '-o', self._full_path(output), self._full_path(source_file)])
    else:
      raise Exception('Unknown file extension: %s' % ext)
    return output

  def insert_sources(self, index, location):
    # Add compression extension.
    distname = self._pkg['distfiles'][index]
    if distname + '.gz' in DISTFILES:
      distname = distname + '.gz'
    elif distname + '.xz' in DISTFILES:
      distname = distname + '.xz'
    copy_file_or_tree(get_patched(distname), self._full_path(location), True)

  def install(self, source, target):
    print('INSTALL', source, '->', target)
    copy_file_or_tree(self._full_path(source),
                      os.path.join(self._install_directory, target), False)

  def link_library(self, object_files):
    objs = [self._full_path(f) for f in sorted(object_files)]
    output = 'lib%d.a' % self._library_number
    print('AR', output)
    self._library_number = self._library_number + 1
    self.run_command('.',
                     [self._env_ar, '-rcs', self._full_path(output)] + objs)
    return output

  def run_command(self, cwd, command):
    os.chdir(os.path.join(self._full_path(cwd)))
    subprocess.check_call(['env', '-i'] + self._env_vars + command)

def build_package(pkg):
  if pkg['name'] in PACKAGES_BUILT:
    return
  if pkg['name'] in PACKAGES_BUILDING:
    raise Exception('Cyclic dependency on package %s' % pkg['name'])
  PACKAGES_BUILDING.add(pkg['name'])
  for dep in pkg['lib_depends']:
    build_package(PACKAGES[dep])

  build_directory = os.path.join(DIR_BUILD, pkg['name'])
  install_directory = os.path.join(DIR_INSTALL, pkg['name'])
  if not os.path.isdir(install_directory):
    print('PKG', pkg['name'])
    pkg['build_cmd'](PackageBuilder(pkg, build_directory, install_directory))
  try:
    shutil.rmtree(build_directory)
  except:
    pass

  PACKAGES_BUILDING.remove(pkg['name'])
  PACKAGES_BUILT.add(pkg['name'])

# Clean up.
try:
  shutil.rmtree(DIR_BUILD)
except:
  pass
try:
  shutil.rmtree(DIR_SOURCES)
except:
  pass
try:
  os.makedirs(DIR_DISTFILES)
except:
  pass

if len(sys.argv) > 1:
  # Only build the packages provided on the command line.
  packages = set(sys.argv[1:])
  for pkg in packages:
    try:
      shutil.rmtree(os.path.join(DIR_INSTALL, pkg))
    except:
      pass
  for pkg in packages:
    build_package(PACKAGES[pkg])
else:
  # Build all packages.
  try:
    shutil.rmtree(DIR_INSTALL)
  except:
    pass
  for pkg in PACKAGES:
    build_package(PACKAGES[pkg])
