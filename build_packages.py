#!/usr/bin/env python3

import fileinput
import hashlib
import os
import random
import shutil
import stat
import subprocess
import sys

DIR_ROOT = os.getcwd()
DIR_BUILD = os.path.join(DIR_ROOT, '_obj/build')
DIR_DEPS = os.path.join(DIR_ROOT, '_obj/deps')
DIR_DISTFILES = os.path.join(DIR_ROOT, '_obj/distfiles')
DIR_INSTALL = os.path.join(DIR_ROOT, '_obj/install')
DIR_REPOSITORY = os.path.join(DIR_ROOT, 'packages')
DIR_SOURCES = os.path.join(DIR_ROOT, '_obj/sources')

PACKAGES = {}
PACKAGES_BUILT = set()
PACKAGES_BUILDING = set()

def build_nothing(ctx):
  pass

def package(**kwargs):
  name = kwargs['name']
  if name in PACKAGES:
    raise Exception('%s listed multiple times' % name)
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

def autoconf_automake_build(ctx):
  ctx.insert_sources(0, '.')
  ctx.run_autoconf()
  ctx.run_make()
  ctx.run_make_install()

def sourceforge_sites(suffix):
  return {fmt + suffix + '/' for fmt in {
      'http://downloads.sourceforge.net/project/',
      'http://freefr.dl.sourceforge.net/project/',
      'http://heanet.dl.sourceforge.net/project/',
      'http://internode.dl.sourceforge.net/project/',
      'http://iweb.dl.sourceforge.net/project/',
      'http://jaist.dl.sourceforge.net/project/',
      'http://kent.dl.sourceforge.net/project/',
      'http://master.dl.sourceforge.net/project/',
      'http://nchc.dl.sourceforge.net/project/',
      'http://ncu.dl.sourceforge.net/project/',
      'http://netcologne.dl.sourceforge.net/project/',
      'http://superb-dca3.dl.sourceforge.net/project/',
      'http://switch.dl.sourceforge.net/project/',
      'http://tenet.dl.sourceforge.net/project/',
      'http://ufpr.dl.sourceforge.net/project/',
  }}

def walk_files(path):
  if os.path.isdir(path):
    for root, dirs, files in os.walk(path):
      for f in files:
        yield (root, f)
  else:
    yield os.path.split(path)

def walk_files_concurrently(source, target):
  for dirname, filename in walk_files(source):
    source_filename = os.path.join(dirname, filename)
    target_filename = os.path.normpath(
        os.path.join(target, os.path.relpath(source_filename, source)))
    yield source_filename, target_filename

# Parse all of the BUILD rules.
for dirname, filename in walk_files(DIR_REPOSITORY):
  if filename == 'BUILD':
    with open(os.path.join(dirname, 'BUILD'), 'r') as f:
      exec(f.read())

def make_parents(path):
  try:
    os.makedirs(os.path.dirname(path))
  except:
    pass

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
    # Delete .orig files that are left behind.
    for dirname, filename in walk_files(source_directory):
      if filename.endswith('.orig'):
        os.unlink(os.path.join(dirname, filename))
    open(dot_patched, 'w').close()
  return source_directory

def copy_file_or_tree(source, target):
  for source_file, target_file in walk_files_concurrently(source, target):
    # Never overwrite any files.
    if os.path.exists(target_file):
      raise Exception('About to overwrite %s with %s' %
                      (target_file, source_file))
    make_parents(target_file)
    shutil.copy2(source_file, target_file)

class PackageBuilder:

  # Fake root directory prefix that is passed to build systems such as
  # Autoconf and Automake, so that they cannot hardcode paths to actual
  # files on the system.
  _FAKE_ROOTDIR = '/nonexistent'

  def __init__(self, pkg, install_directory):
    self._pkg = pkg
    self._install_directory = install_directory
    self._sequence_number = 0

    self._env_ar = '/usr/local/bin/x86_64-unknown-cloudabi-ar'
    self._env_cc = '/usr/local/bin/x86_64-unknown-cloudabi-cc'
    self._env_cxx = '/usr/local/bin/x86_64-unknown-cloudabi-c++'
    self._env_cflags = [
        '-nostdlibinc', '-O2', '-fstack-protector-strong',
        '-Werror=implicit-function-declaration',
        '-Qunused-arguments', '-I%s/include' % DIR_DEPS]
    self._env_cxxflags = self._env_cflags + [
        '-nostdlibinc', '-nostdinc++', '-I%s/include/c++/v1' % DIR_DEPS]
    self._env_vars = [
        'AR=' + self._env_ar,
        'CC=' + self._env_cc,
        'CXX=' + self._env_cxx,
        'CFLAGS=' + ' '.join(self._env_cflags),
        'CPPFLAGS=-I%s/include' % DIR_DEPS,
        'CXXFLAGS=-nostdlibinc ' + ' '.join(self._env_cxxflags),
        'LDFLAGS=-nostdlib -L%s/lib' % DIR_DEPS,
        'NM=/usr/local/bin/x86_64-unknown-cloudabi-nm',
        'OBJDUMP=/usr/local/bin/x86_64-unknown-cloudabi-objdump',
        'PATH=/bin:/sbin:/usr/bin:/usr/sbin',
        'PKG_CONFIG=/usr/local/bin/pkg-config',
        'PKG_CONFIG_LIBDIR=' + os.path.join(DIR_DEPS, 'lib/pkgconfig'),
        'RANLIB=/usr/local/bin/x86_64-unknown-cloudabi-ranlib',
        'STRIP=/usr/local/bin/x86_64-unknown-cloudabi-strip',
    ]

  def _full_path(self, path):
    return os.path.join(DIR_BUILD, path)

  def _some_file(self, fmt):
    filename = fmt % self._sequence_number
    self._sequence_number += 1
    return filename

  def compile(self, source_file, cflags=[]):
    ext = os.path.splitext(source_file)[1]
    output = source_file + '.o'
    if ext in {'.c', '.S'}:
      print('CC', source_file)
      self.run_command(
          '.',
          [self._env_cc] + self._env_cflags + cflags +
          ['-c', '-o', output, source_file])
    elif ext == '.cpp':
      print('CXX', source_file)
      self.run_command(
          '.',
          [self._env_cxx] + self._env_cxxflags + cflags +
          ['-c', '-o', output, source_file])
    else:
      raise Exception('Unknown file extension: %s' % ext)
    return output

  def insert_sources(self, index, location):
    # Add compression extension.
    distname = self._pkg['distfiles'][index]
    if distname + '.bz2' in DISTFILES:
      distname = distname + '.bz2'
    elif distname + '.gz' in DISTFILES:
      distname = distname + '.gz'
    elif distname + '.xz' in DISTFILES:
      distname = distname + '.xz'
    copy_file_or_tree(get_patched(distname), self._full_path(location))

  def install(self, source, target):
    print('INSTALL', source, '->', target)
    target = os.path.join(self._install_directory, target)
    source = self._full_path(source)
    for source_file, target_file in walk_files_concurrently(source, target):
      make_parents(target_file)
      ext = os.path.splitext(source_file)[1]
      if ext == '.a':
        # Remove timestamps from .a header, for determinism.
        shutil.copyfile(source_file, target_file)
        with open(target_file, 'r+') as f:
          f.seek(24)
          f.write("0           ")
      elif ext in {'.la', '.pc'}:
        # Remove references to /nonexistent and DIR_DEPS from libtool
        # archives and pkg-config files.
        with open(source_file, 'r') as f:
          contents = f.read()
        contents = (contents
            .replace('/nonexistent', '%%PREFIX%%')
            .replace(DIR_DEPS, '%%PREFIX%%'))
        with open(target_file + '.template', 'w') as f:
          f.write(contents)
      else:
        # Copy other files literally.
        shutil.copy(source_file, target_file)

  def link_library(self, object_files):
    objs = [self._full_path(f) for f in sorted(object_files)]
    output = self._some_file('lib%d.a')
    print('AR', output)
    self.run_command('.',
                     [self._env_ar, '-rcs', self._full_path(output)] + objs)
    return output

  def remove(self, path):
    path = self._full_path(path)
    if os.path.isdir(path):
      shutil.rmtree(self._full_path(path))
    else:
      os.remove(path)

  def run_autoconf(self, args=[]):
    # Replace config.sub files by an up-to-datecopy.
    for dirname, filename in walk_files(DIR_BUILD):
      if filename == 'config.sub':
        shutil.copy2(os.path.join(DIR_ROOT, 'misc/config.sub'),
                     os.path.join(dirname, 'config.sub'))
    self.run_command('.', ['./configure', '--host=x86_64-unknown-cloudabi',
                           '--prefix=' + self._FAKE_ROOTDIR] + args)

  def run_command(self, cwd, command):
    os.chdir(os.path.join(self._full_path(cwd)))
    subprocess.check_call(['env', '-i'] + self._env_vars + command)

  def run_make(self, args=['all']):
    self.run_command('.', ['make'] + args)

  def run_make_install(self, args=['install']):
    stagedir = self._some_file('stage%d')
    self.run_command('.',
                     ['make', 'DESTDIR=' + self._full_path(stagedir)] + args)
    self.install(os.path.join(stagedir, self._FAKE_ROOTDIR[1:]), '.')

def _copy_dependencies(pkg, done):
  for dep in pkg['lib_depends']:
    if dep not in done:
      source = os.path.join(DIR_INSTALL, dep)
      if os.path.exists(source):
        # Install files from package into dependency directory.
        for source_file, target_file in walk_files_concurrently(source,
                                                                DIR_DEPS):
          make_parents(target_file)
          if target_file.endswith('.template'):
            # File is a template. Expand %%PREFIX%% tags.
            with open(source_file, 'r') as f:
              contents = f.read()
            contents = contents.replace('%%PREFIX%%', DIR_DEPS)
            with open(target_file[:-9], 'w') as f:
              f.write(contents)
          else:
            # Regular file. Copy it over literally.
            shutil.copy(source_file, target_file)

      done.add(dep)
      _copy_dependencies(PACKAGES[dep], done)

def copy_dependencies(pkg):
  _copy_dependencies(pkg, set())

def build_package(pkg):
  if pkg['name'] in PACKAGES_BUILT:
    return
  if pkg['name'] in PACKAGES_BUILDING:
    raise Exception('Cyclic dependency on package %s' % pkg['name'])
  PACKAGES_BUILDING.add(pkg['name'])
  for dep in pkg['lib_depends']:
    build_package(PACKAGES[dep])

  # Clean up.
  try:
    shutil.rmtree(DIR_BUILD)
  except:
    pass
  try:
    shutil.rmtree(DIR_DEPS)
  except:
    pass

  install_directory = os.path.join(DIR_INSTALL, pkg['name'])
  if 'build_cmd' in pkg and not os.path.isdir(install_directory):
    # Install dependencies into a temporary directory.
    print('PKG', pkg['name'])
    copy_dependencies(pkg)
    pkg['build_cmd'](PackageBuilder(pkg, install_directory))

  PACKAGES_BUILDING.remove(pkg['name'])
  PACKAGES_BUILT.add(pkg['name'])

# Clean up.
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
  for pkg in PACKAGES:
    build_package(PACKAGES[pkg])
