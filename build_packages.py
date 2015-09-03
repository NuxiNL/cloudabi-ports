#!/usr/bin/env python3

import fileinput
import hashlib
import os
import random
import shutil
import stat
import subprocess
import sys

# Fixed directories where we want to do the build and provide
# dependencies. These directories must not change, as this breaks the
# reproducibility of the generated packages.
DIR_BUILD = '/usr/obj/cloudabi-ports'

# Locations relative to the source tree.
DIR_ROOT = os.getcwd()
DIR_DISTFILES = os.path.join(DIR_ROOT, '_obj/distfiles')
DIR_INSTALL = os.path.join(DIR_ROOT, '_obj/install')
DIR_REPOSITORY = os.path.join(DIR_ROOT, 'packages')
DIR_SOURCES = os.path.join(DIR_ROOT, '_obj/sources')

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
  DISTFILES[name] = kwargs

def autoconf_automake_build(root):
  root.insert_sources()
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

class BuildAccess:
  def __init__(self, builder, distfiles, path):
    self._builder = builder
    self._distfiles = distfiles
    self._path = path

  def archive(self, objects):
    return BuildAccess(self._builder, self._distfiles,
                       self._builder.archive(obj._path for obj in objects))

  def autoconf(self, args=[]):
    # Replace config.sub files by an up-to-date copy.
    for dirname, filename in walk_files(self._path):
      if filename == 'config.sub':
        shutil.copy(os.path.join(DIR_ROOT, 'misc/config.sub'),
                    os.path.join(dirname, 'config.sub'))

    # Run the configure script in a separate directory.
    builddir = self._builder.get_new_tmpdir()
    self._builder.autoconf(
        builddir, os.path.join(self._path, 'configure'), args)
    return BuildAccess(self._builder, self._distfiles, builddir)

  def compile(self, args=[]):
    output = self._path + '.o'
    self._builder.compile(self._path, output, args)
    return BuildAccess(self._builder, self._distfiles, output)

  def cmake(self, args=[]):
    builddir = self._builder.get_new_tmpdir()
    self._builder.cmake(builddir, self._path, args)
    return BuildAccess(self._builder, self._distfiles, builddir)

  def insert_sources(self, index=0):
    # Add compression extension.
    # TODO(ed): Maybe this should be done earlier on.
    distname = self._distfiles[index]
    if distname + '.bz2' in DISTFILES:
      distname = distname + '.bz2'
    elif distname + '.gz' in DISTFILES:
      distname = distname + '.gz'
    elif distname + '.xz' in DISTFILES:
      distname = distname + '.xz'
    for source_file, target_file in walk_files_concurrently(
        get_patched(distname), self._path):
      make_parents(target_file)
      copy_file(source_file, target_file)
      try:
        shutil.copystat(source_file, target_file)
      except:
        pass

  def install(self, path='.'):
    self._builder.install(self._path, path)

  def make(self, args=['all'], gnu_make=False):
    self._builder.run(self._path,
                      ['gmake' if gnu_make else 'make', '-j6'] + args)

  def make_install(self, args=['install']):
    return BuildAccess(self._builder, self._distfiles,
                       self._builder.make_install(self._path, args))

  def path(self, path):
    return BuildAccess(self._builder, self._distfiles,
                       os.path.join(self._path, path))

  def remove(self):
    try:
      shutil.rmtree(self._path)
    except:
      os.unlink(self._path)

  def run(self, command):
    self._builder.run(self._path, command)

  def symlink(self, contents):
    os.symlink(contents, self._path)

  def unhardcode_paths(self):
    self._builder.unhardcode_paths(self._path)

class Builder:
  def __init__(self, build_directory):
    self._build_directory = build_directory
    self._sequence_number = 0

  def get_new_archive(self):
    path = os.path.join(self._build_directory, 'tmp',
                        'lib%d.a' % self._sequence_number)
    self._sequence_number += 1
    make_parents(path)
    return path

  def get_new_tmpdir(self):
    path = os.path.join(self._build_directory, 'tmp',
                        str(self._sequence_number))
    self._sequence_number += 1
    return path

class PackageBuilder(Builder):
  def __init__(self, pkg, build_directory, install_directory, arch):
    super(PackageBuilder, self).__init__(build_directory)

    self._pkg = pkg
    self._install_directory = install_directory
    self._arch = arch

    self._prefix = os.path.join(DIR_BUILD, self._arch)
    self._cflags = ['-O2', '-fstack-protector-strong',
                    '-Werror=implicit-function-declaration']

  def _tool(self, name):
    return os.path.join(DIR_BUILD, 'bin', '%s-%s' % (self._arch, name))

  def archive(self, object_files):
    objs = sorted(object_files)
    output = self.get_new_archive()
    print('AR', output)
    self.run('.', [self._tool('ar'), '-rcs', output] + objs)
    return output

  def autoconf(self, builddir, script, args):
    self.run(builddir,
             [script, '--host=' + self._arch, '--prefix=/nonexistent'] + args)

  def cmake(self, builddir, sourcedir, args):
    self.run(builddir, [
        '/usr/local/bin/cmake', sourcedir,
        '-DCMAKE_AR=' + self._tool('ar'),
        '-DCMAKE_BUILD_TYPE=Release',
        '-DCMAKE_INSTALL_PREFIX=/nonexistent',
        '-DCMAKE_RANLIB=' + self._tool('ranlib')] + args)

  def compile(self, source, target, args):
    os.chdir(os.path.dirname(source))
    ext = os.path.splitext(source)[1]
    if ext in {'.c', '.S'}:
      print('CC', source)
      self.run(
          '.',
          [self._tool('cc')] + self._cflags + args +
          ['-c', '-o', target, source])
    elif ext == '.cpp':
      print('CXX', source)
      self.run(
          '.',
          [self._tool('c++')] + self._cflags + args +
          ['-c', '-o', target, source])
    else:
      raise Exception('Unknown file extension: %s' % ext)

  def _unhardcode(self, source, target):
    with open(source, 'r') as f:
      contents = f.read()
    contents = (contents
        .replace('/nonexistent', '%%PREFIX%%')
        .replace(self._prefix, '%%PREFIX%%'))
    with open(target, 'w') as f:
      f.write(contents)

  def unhardcode_paths(self, path):
    self._unhardcode(path, path + '.template')
    shutil.copymode(path, path + '.template')
    os.unlink(path)

  def install(self, source, target):
    print('INSTALL', source, '->', target)
    target = os.path.join(self._install_directory, target)
    for source_file, target_file in walk_files_concurrently(source, target):
      make_parents(target_file)
      ext = os.path.splitext(source_file)[1]
      if ext in {'.la', '.pc'}:
        # Remove references to /nonexistent and /usr/obj from libtool
        # archives and pkg-config files.
        self._unhardcode(source_file, target_file + '.template')
      else:
        # Copy other files literally.
        copy_file(source_file, target_file)

  def make_install(self, path, args):
    stagedir = self.get_new_tmpdir()
    self.run(path, ['make', 'DESTDIR=' + stagedir] + args)
    return os.path.join(stagedir, 'nonexistent')

  def run(self, cwd, command):
    try:
      os.makedirs(cwd)
    except:
      pass
    os.chdir(os.path.join(cwd))
    subprocess.check_call([
        'env', '-i',
        'AR=' + self._tool('ar'),
        'CC=' + self._tool('cc'),
        'CXX=' + self._tool('c++'),
        'CFLAGS=' + ' '.join(self._cflags),
        'NM=' + self._tool('nm'),
        'OBJDUMP=' + self._tool('objdump'),
        'PATH=%s/bin:/bin:/sbin:/usr/bin:/usr/sbin' % DIR_BUILD,
        'PKG_CONFIG=/usr/local/bin/pkg-config',
        'PKG_CONFIG_LIBDIR=' + os.path.join(self._prefix, 'lib/pkgconfig'),
        'RANLIB=' + self._tool('ranlib'),
        'STRIP=' + self._tool('strip')] + command)

class HostPackageBuilder(Builder):
  def __init__(self, build_directory, install_directory):
    super(HostPackageBuilder, self).__init__(build_directory)

    self._install_directory = install_directory

  def autoconf(self, builddir, script, args):
    self.run(builddir, [script, '--prefix=' + DIR_BUILD] + args)

  def cmake(self, builddir, sourcedir, args):
    self.run(builddir, ['cmake', sourcedir,
                        '-DCMAKE_BUILD_TYPE=Release',
                        '-DCMAKE_INSTALL_PREFIX=' + DIR_BUILD] + args)

  def install(self, source, target):
    print('INSTALL', source, '->', target)
    target = os.path.join(self._install_directory, target)
    for source_file, target_file in walk_files_concurrently(source, target):
      make_parents(target_file)
      copy_file(source_file, target_file)

  def make_install(self, path, args):
    stagedir = self.get_new_tmpdir()
    self.run(path, ['make', 'DESTDIR=' + stagedir] + args)
    return os.path.join(stagedir, DIR_BUILD[1:])

  def run(self, cwd, command):
    try:
      os.makedirs(cwd)
    except:
      pass
    os.chdir(cwd)
    subprocess.check_call(command)

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

    build_directory = os.path.join(DIR_BUILD, arch, pkg['name'])
    pkg['build_cmd'](BuildAccess(PackageBuilder(
        pkg, build_directory, install_directory, arch),
        pkg['distfiles'], build_directory))

  PACKAGES_BUILDING.remove(pkg['name'])
  PACKAGES_BUILT.add(pkg['name'])

def build_host_package(pkg):
  try:
    shutil.rmtree(DIR_BUILD)
  except:
    pass
  build_directory = os.path.join(DIR_BUILD, 'host', pkg['name'])
  install_directory = os.path.join(DIR_INSTALL, 'host', pkg['name'])
  if not os.path.isdir(install_directory):
    print('PKG', pkg['name'], 'host')
    pkg['build_cmd'](BuildAccess(HostPackageBuilder(
        build_directory, install_directory), pkg['distfiles'], build_directory))

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
    for arch in ARCHITECTURES:
      build_package(PACKAGES[pkg], arch)
else:
  # Build all packages.
  for pkg in HOST_PACKAGES:
    build_host_package(HOST_PACKAGES[pkg])
  for pkg in PACKAGES:
    for arch in ARCHITECTURES:
      build_package(PACKAGES[pkg], arch)
