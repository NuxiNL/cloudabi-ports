# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import logging
import os
import random
import shutil
import string
import subprocess

from . import config
from . import util

from src.distfile import Distfile
from src.version import SimpleVersion
from typing import Any, Dict, List, Optional
log = logging.getLogger(__name__)


def _chdir(path: str) -> None:
    util.make_dir(path)
    os.chdir(path)


class DiffCreator:
    def __init__(self, source_directory, build_directory, filename):
        self._source_directory = source_directory
        self._build_directory = build_directory
        self._filename = filename

    def __enter__(self):
        # Create a backup of the source directory.
        self._backup_directory = self._build_directory.get_new_directory()
        for source_file, backup_file in util.walk_files_concurrently(
                self._source_directory, self._backup_directory):
            util.make_parent_dir(backup_file)
            util.copy_file(source_file, backup_file, False)

    def __exit__(self, type, value, traceback):
        # Create a diff to store the changes that were made to the original.
        util.diff(self._backup_directory, self._source_directory,
                  self._filename)


class FileHandle:
    def __init__(self, builder: 'Builder', path: str) -> None:
        self._builder = builder
        self._path = path

    def __str__(self):
        return self._path

    def autoreconf(self):
        self.run(['autoreconf', '-i'])

    def gnu_configure(self, args=[], inplace=False):
        for path in util.walk_files(self._path):
            filename = os.path.basename(path)
            if filename in {'config.guess', 'config.sub'}:
                # Replace the config.guess and config.sub files by
                # up-to-date copies. The copies provided by the tarball
                # rarely support CloudABI.
                os.unlink(path)
                shutil.copy(os.path.join(config.DIR_RESOURCES, filename), path)
            elif filename == 'ltmain.sh':
                # Patch up libtool to archive object files in sorted
                # order. This has been fixed in the meantime.
                with open(path, 'r') as fin, open(path + '.new', 'w') as fout:
                    for l in fin.readlines():
                        # Add sort to the pipeline.
                        fout.write(
                            l.replace('-print | $NL2SP',
                                      '-print | sort | $NL2SP'))
                shutil.copymode(path, path + '.new')
                os.rename(path + '.new', path)
            elif filename == 'configure':
                # Patch up configure scripts to remove constructs that are known
                # to fail, for example due to functions being missing.
                with open(path, 'rb') as fin, open(path + '.new',
                                                   'wb') as fout:
                    for l in fin.readlines():
                        # Bad C99 features test.
                        if l.startswith(b'#define showlist(...)'):
                            l = b'#define showlist(...) fputs (stderr, #__VA_ARGS__)\n'
                        elif l.startswith(b'#define report(test,...)'):
                            l = b'#define report(...) fprintf (stderr, __VA_ARGS__)\n'
                        fout.write(l)
                shutil.copymode(path, path + '.new')
                os.rename(path + '.new', path)

        # Run the configure script in a separate directory.
        builddir = (self._path if inplace else
                    self._builder._build_directory.get_new_directory())
        self._builder.gnu_configure(builddir,
                                    os.path.join(self._path, 'configure'),
                                    args)
        return FileHandle(self._builder, builddir)

    def compile(self, args=[]):
        output = self._path + '.o'
        os.chdir(os.path.dirname(self._path))
        ext = os.path.splitext(self._path)[1]
        if ext in {'.c', '.S'}:
            log.info('CC %s', self._path)
            subprocess.check_call([self._builder.get_cc()
                                   ] + self._builder.get_cflags() + args +
                                  ['-c', '-o', output, self._path])
        elif ext in {'.cc', '.cpp'}:
            log.info('CXX %s', self._path)
            subprocess.check_call([self._builder.get_cxx()
                                   ] + self._builder.get_cxxflags() + args +
                                  ['-c', '-o', output, self._path])
        else:
            raise Exception('Unknown file extension: %s' % ext)
        return FileHandle(self._builder, output)

    def debug_shell(self):
        self.run([
            'HOME=' + os.getenv('HOME'),
            'LC_CTYPE=' + os.getenv('LC_CTYPE', 'en_US.UTF-8'),
            'TERM=' + os.getenv('TERM'),
            'sh',
        ])

    def diff(self, filename):
        return DiffCreator(self._path, self._builder._build_directory,
                           filename)

    def host(self):
        return FileHandle(self._builder._host_builder, self._path)

    def rename(self, dst):
        os.rename(self._path, dst._path)

    def cmake(self, args: List[str] = []) -> 'FileHandle':
        builddir = self._builder._build_directory.get_new_directory()
        self._builder.cmake(builddir, self._path, args)
        return FileHandle(self._builder, builddir)

    def install(self, path: str = '.') -> None:
        self._builder.install(self._path, path)

    def make(self, args=['all']):
        self.run(['make', '-j6'] + args)

    def make_install(self, args=['install']):
        stagedir = self._builder._build_directory.get_new_directory()
        self.run(['make', 'DESTDIR=' + stagedir] + args)
        return FileHandle(self._builder,
                          os.path.join(stagedir,
                                       self._builder.get_prefix()[1:]))

    def ninja(self) -> None:
        self.run(['ninja'])

    def ninja_install(self):
        stagedir = self._builder._build_directory.get_new_directory()
        self.run(['DESTDIR=' + stagedir, 'ninja', 'install'])
        return FileHandle(self._builder,
                          os.path.join(stagedir,
                                       self._builder.get_prefix()[1:]))

    def open(self, mode):
        return open(self._path, mode)

    def path(self, path: str) -> 'FileHandle':
        return FileHandle(self._builder, os.path.join(self._path, path))

    def remove(self):
        util.remove(self._path)

    def run(self, command: List[str]) -> None:
        self._builder.run(self._path, command)

    def symlink(self, contents):
        util.remove(self._path)
        util.make_parent_dir(self._path)
        os.symlink(contents, self._path)

    def unhardcode_paths(self):
        self._builder.unhardcode_paths(self._path)


class BuildHandle:
    def __init__(self, builder: 'Builder', name: str, version: SimpleVersion, distfiles: Dict[str, Distfile], resource_directory: str) -> None:
        self._builder = builder
        self._name = name
        self._version = version
        self._distfiles = distfiles
        self._resource_directory = resource_directory

    def archive(self, objects):
        return FileHandle(self._builder,
                          self._builder.archive(obj._path for obj in objects))

    def cc(self):
        return self._builder.get_cc()

    def cflags(self):
        return ' '.join(self._builder.get_cflags())

    def cpu(self):
        return self._builder.get_cpu()

    def cxx(self):
        return self._builder.get_cxx()

    def cxxflags(self):
        return ' '.join(self._builder.get_cxxflags())

    @staticmethod
    def endian():
        # TODO(ed): Extend this once we support big endian CPUs as well.
        return 'little'

    def executable(self, objects):
        objs = sorted(obj._path for obj in objects)
        output = self._builder._build_directory.get_new_executable()
        log.info('LD %s', output)
        subprocess.check_call([self._builder.get_cc(), '-o', output] + objs)
        return FileHandle(self._builder, output)

    def extract(self, name: str = '%(name)s-%(version)s') -> FileHandle:
        return FileHandle(
            self._builder, self._distfiles[name % {
                'name': self._name,
                'version': self._version
            }].extract(self._builder._build_directory.get_new_directory()))

    def gnu_triple(self):
        return self._builder.get_gnu_triple()

    def host(self):
        return BuildHandle(self._builder._host_builder, self._name,
                           self._version, self._distfiles,
                           self._resource_directory)

    def localbase(self):
        return self._builder.get_localbase()

    def prefix(self):
        return self._builder.get_prefix()

    def resource(self, name):
        source = os.path.join(self._resource_directory, name)
        target = os.path.join(config.DIR_BUILDROOT, 'build', name)
        util.make_parent_dir(target)
        util.copy_file(source, target, False)
        return FileHandle(self._builder, target)

    @staticmethod
    def stack_direction():
        # TODO(ed): Don't hardcode this.
        return 'down'


class BuildDirectory:
    def __init__(self) -> None:
        self._sequence_number = 0
        self._builddir = os.path.join(config.DIR_BUILDROOT, 'build')

    def get_new_archive(self):
        path = os.path.join(self._builddir, 'lib%d.a' % self._sequence_number)
        util.make_parent_dir(path)
        self._sequence_number += 1
        return path

    def get_new_directory(self) -> str:
        path = os.path.join(self._builddir, str(self._sequence_number))
        util.make_dir(path)
        self._sequence_number += 1
        return path

    def get_new_executable(self):
        path = os.path.join(self._builddir, 'bin%d' % self._sequence_number)
        util.make_parent_dir(path)
        self._sequence_number += 1
        return path


class Abstract(NotImplementedError):
    pass  # TODO: use abc?


class Builder:
    def __init__(self, build_directory: BuildDirectory,
                 install_directory: Optional[str]) -> None:
        self._build_directory = build_directory
        self._install_directory = install_directory

    def cmake(self, builddir: str, srcdir: str,
              args: List[str]) -> None: raise Abstract()

    def install(self, source: str, target: str) -> None: raise Abstract()

    def run(self, cwd: str, command: List[str]) -> None: raise Abstract()


class HostBuilder(Builder):
    def __init__(self, build_directory: BuildDirectory, install_directory: str) -> None:
        self._build_directory = build_directory
        self._install_directory = install_directory

        self._cflags = [
            '-O2',
            '-I' + os.path.join(self.get_prefix(), 'include'),
        ]

    def gnu_configure(self, builddir, script, args):
        self.run(builddir, [script, '--prefix=' + self.get_prefix()] + args)

    def cmake(self, builddir: str, sourcedir: str, args: List[str]) -> None:
        self.run(builddir, [
            'cmake',
            sourcedir,
            '-G',
            'Ninja',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_FIND_ROOT_PATH=' + self.get_prefix(),
            '-DCMAKE_INSTALL_PREFIX=' + self.get_prefix(),
        ] + args)

    @staticmethod
    def get_cc() -> str:
        return config.HOST_CC

    def get_cflags(self):
        return self._cflags

    @staticmethod
    def get_cxx() -> str:
        return config.HOST_CXX

    @staticmethod
    def get_gnu_triple():
        # Run config.guess to determine the GNU triple of the system
        # we're running on.
        config_guess = os.path.join(config.DIR_RESOURCES, 'config.guess')
        triple = subprocess.check_output(config_guess)
        return str(triple, encoding='ASCII').strip()

    @staticmethod
    def get_prefix() -> str:
        return config.DIR_BUILDROOT

    def install(self, source: str, target: str) -> None:
        log.info('INSTALL %s->%s', source, target)
        target = os.path.join(self._install_directory, target)
        for source_file, target_file in util.walk_files_concurrently(
                source, target):
            # As these are bootstrapping tools, there is no need to
            # preserve any documentation and locales.
            path = os.path.relpath(target_file, target)
            if (path != 'lib/charset.alias'
                    and not path.startswith('share/doc/')
                    and not path.startswith('share/info/')
                    and not path.startswith('share/locale/')
                    and not path.startswith('share/man/')):
                util.make_parent_dir(target_file)
                util.copy_file(source_file, target_file, False)

    def run(self, cwd: str, command: List[str]) -> None:
        _chdir(cwd)
        subprocess.check_call([
            'env',
            'CC=' + self.get_cc(),
            'CXX=' + self.get_cxx(),
            'CFLAGS=' + ' '.join(self._cflags),
            'CXXFLAGS=' + ' '.join(self._cflags),
            'LDFLAGS=-L' + os.path.join(self.get_prefix(), 'lib'),
            'PATH=%s:%s' % (os.path.join(self.get_prefix(), 'bin'),
                            os.getenv('PATH')),
        ] + command)


class TargetBuilder(Builder):
    def __init__(self, build_directory, install_directory, arch):
        self._build_directory = build_directory
        self._install_directory = install_directory
        self._arch = arch

        # Pick a random prefix directory. That way the build will fail
        # due to nondeterminism in case our piece of software hardcodes
        # the prefix directory.
        self._prefix = '/' + ''.join(
            random.choice(string.ascii_letters) for i in range(16))

        self._bindir = os.path.join(config.DIR_BUILDROOT, 'bin')
        self._localbase = os.path.join(config.DIR_BUILDROOT, self._arch)
        self._cflags = [
            '-O2',
            '-Werror=implicit-function-declaration',
            '-Werror=date-time',
        ]

        # In case we need to build software for the host system.
        self._host_builder = HostBuilder(build_directory, None)

    def _tool(self, name):
        return os.path.join(self._bindir, '%s-%s' % (self._arch, name))

    def archive(self, object_files):
        objs = sorted(object_files)
        output = self._build_directory.get_new_archive()
        log.info('AR %s', output)
        subprocess.check_call([self._tool('ar'), '-rcs', output] + objs)
        return output

    def gnu_configure(self, builddir, script, args):
        self.run(
            builddir,
            [script, '--host=' + self._arch, '--prefix=' + self.get_prefix()] +
            args)

    def cmake(self, builddir, sourcedir, args):
        self.run(builddir, [
            'cmake',
            sourcedir,
            '-G',
            'Ninja',
            '-DCMAKE_AR=' + self._tool('ar'),
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_FIND_ROOT_PATH=' + self._localbase,
            '-DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY',
            '-DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=ONLY',
            '-DCMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER',
            '-DCMAKE_INSTALL_PREFIX=' + self.get_prefix(),
            '-DCMAKE_NO_SYSTEM_FROM_IMPORTED=ON',
            '-DCMAKE_PREFIX_PATH=' + self._localbase,
            '-DCMAKE_RANLIB=' + self._tool('ranlib'),
            '-DCMAKE_SYSTEM_NAME=Generic',
            '-DCMAKE_SYSTEM_PROCESSOR=' + self._arch.split('-')[0],
            '-DPROTOBUF_IMPORT_DIRS=%s/include' % self._localbase,
            '-DUNIX=YES',
        ] + args)

    def get_cc(self):
        return self._tool('cc')

    def get_cflags(self):
        return self._cflags

    def get_cpu(self):
        return self._arch.split('-', 1)[0]

    def get_cxx(self):
        return self._tool('c++')

    def get_cxxflags(self):
        return self._cflags

    def get_gnu_triple(self):
        return self._arch

    def get_localbase(self):
        return self._localbase

    def get_prefix(self):
        return self._prefix

    def _unhardcode(self, source, target):
        assert not os.path.islink(source)
        with open(source, 'r') as f:
            contents = f.read()
        contents = (contents.replace(self.get_prefix(), '%%PREFIX%%').replace(
            self._localbase, '%%PREFIX%%'))
        with open(target, 'w') as f:
            f.write(contents)

    def unhardcode_paths(self, path):
        self._unhardcode(path, path + '.template')
        shutil.copymode(path, path + '.template')
        os.unlink(path)

    def install(self, source, target):
        log.info('INSTALL %s->%s', source, target)
        target = os.path.join(self._install_directory, target)
        for source_file, target_file in util.walk_files_concurrently(
                source, target):
            util.make_parent_dir(target_file)
            relpath = os.path.relpath(target_file, self._install_directory)
            ext = os.path.splitext(source_file)[1]
            if ext in {'.la', '.pc'} and not os.path.islink(source_file):
                # Remove references to the installation prefix and the
                # localbase directory from libtool archives and
                # pkg-config files.
                self._unhardcode(source_file, target_file + '.template')
            elif ext == '.pyc':
                # Don't install precompiled Python sources. These
                # contain metadata that is non-deterministic.
                pass
            elif relpath.startswith('share/man/') and ext != '.gz':
                # Compress manual pages.
                util.gzip_file(source_file, target_file + '.gz')
            elif relpath == 'share/info/dir':
                # Don't install the GNU Info directory, as it should be
                # regenerated based on the set of packages installed.
                pass
            else:
                # Copy other files literally.
                util.copy_file(source_file, target_file, False)

    def run(self, cwd, command):
        _chdir(cwd)
        subprocess.check_call([
            'env',
            '-i',
            'AR=' + self._tool('ar'),
            'CC=' + self._tool('cc'),
            'CC_FOR_BUILD=' + self._host_builder.get_cc(),
            'CFLAGS=' + ' '.join(self._cflags),
            'CXX=' + self._tool('c++'),
            'CXXFLAGS=' + ' '.join(self._cflags),
            'CXX_FOR_BUILD=' + self._host_builder.get_cxx(),
            'NM=' + self._tool('nm'),
            'OBJDUMP=' + self._tool('objdump'),
            # List tools directory twice, as certain tools and scripts
            # get confused if PATH contains no colon.
            'PATH=%s:%s' % (self._bindir, self._bindir),
            'PERL=' + config.PERL,
            'PKG_CONFIG=' + self._tool('pkg-config'),
            'RANLIB=' + self._tool('ranlib'),
            'STRIP=' + self._tool('strip'),
        ] + command)
