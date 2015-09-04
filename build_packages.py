#!/usr/bin/env python3

import fileinput
import hashlib
import os
import random
import shutil
import stat
import subprocess
import sys

from src import builder

# Fixed directories where we want to do the build and provide
# dependencies. These directories must not change, as this breaks the
# reproducibility of the generated packages.
DIR_BUILD = '/usr/obj/cloudabi-ports'

# Locations relative to the source tree.
DIR_ROOT = os.getcwd()
DIR_DISTFILES = os.path.join(DIR_ROOT, '_obj/distfiles')
DIR_INSTALL = os.path.join(DIR_ROOT, '_obj/install')
DIR_REPOSITORY = os.path.join(DIR_ROOT, 'packages')

PACKAGES = {}
HOST_PACKAGES = {}
PACKAGES_BUILT = set()
PACKAGES_BUILDING = set()

ARCHITECTURES = {'x86_64-unknown-cloudabi'}

def build_nothing(root):
  pass

def host_package(**kwargs):
  pass
  name = kwargs['name']
  if name in HOST_PACKAGES:
    raise Exception('%s listed multiple times' % name)
  if 'distfiles' not in kwargs:
    kwargs['distfiles'] = ['%s-%s.tar' % (kwargs['name'], kwargs['version'])]
  HOST_PACKAGES[name] = kwargs

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
  if 'patches' not in kwargs:
    kwargs['patches'] = set()
  DISTFILES[name] = kwargs

def autoconf_automake_build(ctx):
  root = ctx.distfile()
  build = root.autoconf()
  build.make()
  build.make_install().install()

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

def copy_file(source, target):
  if os.path.exists(target):
    raise Exception('About to overwrite %s with %s' % (source, target))
  if os.path.islink(source):
    # Preserve symbolic links.
    destination = os.readlink(source)
    if os.path.isabs(destination):
      raise Exception('%s points to absolute location %s', source, destination)
    os.symlink(destination, target)
  elif os.path.isfile(source):
    # Copy regular files.
    shutil.copy(source, target)
  else:
    # Bail out on anything else.
    raise Exception(source + ' is of an unsupported type')

def _copy_dependencies(pkg, arch, done):
  for dep in pkg['lib_depends']:
    if dep not in done:
      source = os.path.join(DIR_INSTALL, arch, dep)
      target = os.path.join(DIR_BUILD, arch)
      if os.path.exists(source):
        # Install files from package into dependency directory.
        for source_file, target_file in walk_files_concurrently(
            source, target):
          make_parents(target_file)
          if target_file.endswith('.template'):
            # File is a template. Expand %%PREFIX%% tags.
            target_file = target_file[:-9]
            with open(source_file, 'r') as f:
              contents = f.read()
            contents = contents.replace('%%PREFIX%%', target)
            with open(target_file, 'w') as f:
              f.write(contents)
            shutil.copymode(source_file, target_file)
          else:
            # Regular file. Copy it over literally.
            copy_file(source_file, target_file)

      done.add(dep)
      _copy_dependencies(PACKAGES[dep], arch, done)

def copy_dependencies(pkg, arch):
  _copy_dependencies(pkg, arch, set())

class Distfile:
  def __init__(self, name):
    if name + '.gz' in DISTFILES:
      self._name = name + '.gz'
    elif name + '.bz2' in DISTFILES:
      self._name = name + '.bz2'
    elif name + '.xz' in DISTFILES:
      self._name = name + '.xz'
    else:
      self._name = name

  def patches(self):
    return (os.path.join(DIR_REPOSITORY, f)
            for f in DISTFILES[self._name]['patches'])

  def tarball(self):
    return get_distfile(self._name)

def build_package(pkg, arch):
  if pkg['name'] in PACKAGES_BUILT:
    return
  if pkg['name'] in PACKAGES_BUILDING:
    raise Exception('Cyclic dependency on package %s' % pkg['name'])
  PACKAGES_BUILDING.add(pkg['name'])
  for dep in pkg['lib_depends']:
    build_package(PACKAGES[dep], arch)

  try:
    shutil.rmtree(DIR_BUILD)
  except:
    pass

  install_directory = os.path.join(DIR_INSTALL, arch, pkg['name'])
  if 'build_cmd' in pkg and not os.path.isdir(install_directory):
    print('PKG', pkg['name'], arch)

    # Copy the toolchain into the build directory.
    for dep in HOST_PACKAGES:
      for source, target in walk_files_concurrently(
          os.path.join(DIR_INSTALL, 'host', dep), DIR_BUILD):
        make_parents(target)
        copy_file(source, target)
    # Copy the dependencies into the build directory.
    copy_dependencies(pkg, arch)

    pkg['build_cmd'](builder.BuildHandle(builder.PackageBuilder(
        install_directory, arch),
        [Distfile(d) for d in pkg['distfiles']]))

  PACKAGES_BUILDING.remove(pkg['name'])
  PACKAGES_BUILT.add(pkg['name'])

def build_host_package(pkg):
  try:
    shutil.rmtree(DIR_BUILD)
  except:
    pass
  install_directory = os.path.join(DIR_INSTALL, 'host', pkg['name'])
  if not os.path.isdir(install_directory):
    print('PKG', pkg['name'], 'host')
    pkg['build_cmd'](builder.BuildHandle(builder.HostPackageBuilder(
        install_directory),
        [Distfile(d) for d in pkg['distfiles']]))

# Clean up.
try:
  os.makedirs(DIR_DISTFILES)
except:
  pass

if len(sys.argv) > 1:
  # Only build the packages provided on the command line.
  packages = set(sys.argv[1:])
  for pkg in packages:
    for arch in ARCHITECTURES:
      try:
        shutil.rmtree(os.path.join(DIR_INSTALL, arch, pkg))
      except:
        pass
  for pkg in packages:
    for arch in ARCHITECTURES:
      build_package(PACKAGES[pkg], arch)
else:
  # Build all packages.
  for pkg in HOST_PACKAGES:
    build_host_package(HOST_PACKAGES[pkg])
  for pkg in PACKAGES:
    for arch in ARCHITECTURES:
      build_package(PACKAGES[pkg], arch)
