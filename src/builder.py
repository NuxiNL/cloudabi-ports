import os
import shutil
import subprocess

from . import config
from . import util


def _chdir(path):
    util.make_dir(path)
    os.chdir(path)


class FileHandle:

    def __init__(self, builder, path):
        self._builder = builder
        self._path = path

    def autoconf(self, args=[], inplace=False):
        for dirname, filename in util.walk_files(self._path):
            path = os.path.join(dirname, filename)
            if filename == 'config.sub':
                # Replace config.sub files by an up-to-date copy. The copy
                # provided by the tarball rarely supports CloudABI.
                shutil.copy(os.path.join(
                    config.DIR_RESOURCES, 'config.sub'), path)
            elif filename == 'configure':
                # Patch up configure scripts to remove constructs that are known
                # to fail, for example due to functions being missing.
                with open(path, 'r') as fin:
                    with open(path + '.new', 'w') as fout:
                        for l in fin.readlines():
                            # Bad C99 features test.
                            if l.startswith('#define showlist(...)'):
                                l = '#define showlist(...) fputs (stderr, #__VA_ARGS__)\n'
                            elif l.startswith('#define report(test,...)'):
                                l = '#define report(...) fprintf (stderr, __VA_ARGS__)\n'
                            fout.write(l)
                shutil.copymode(path, path + '.new')
                os.rename(path + '.new', path)

        # Run the configure script in a separate directory.
        builddir = self._path if inplace else self._builder.get_new_directory()
        self._builder.autoconf(
            builddir, os.path.join(self._path, 'configure'), args)
        return FileHandle(self._builder, builddir)

    def compile(self, args=[]):
        output = self._path + '.o'
        self._builder.compile(self._path, output, args)
        return FileHandle(self._builder, output)

    def rename(self, dst):
        os.rename(self._path, dst._path)

    def cmake(self, args=[]):
        builddir = self._builder.get_new_directory()
        self._builder.cmake(builddir, self._path, args)
        return FileHandle(self._builder, builddir)

        # Skip directory names.
        while True:
            entries = os.listdir(source_directory)
            if len(entries) != 1:
                break
            new_directory = os.path.join(source_directory, entries[0])
            if not os.path.isdir(new_directory):
                break
            source_directory = new_directory

    def install(self, path='.'):
        self._builder.install(self._path, path)

    def make(self, args=['all'], gnu_make=False):
        self.run(['gmake' if gnu_make else 'make', '-j6'] + args)

    def make_install(self, args=['install']):
        stagedir = self._builder.get_new_directory()
        self.run(['make', 'DESTDIR=' + stagedir] + args)
        return FileHandle(
            self._builder,
            os.path.join(
                stagedir,
                self._builder.get_prefix()[
                    1:]))

    def path(self, path):
        return FileHandle(self._builder, os.path.join(self._path, path))

    def remove(self):
        util.remove(self._path)

    def run(self, command):
        self._builder.run(self._path, command)

    def symlink(self, contents):
        os.symlink(contents, self._path)

    def unhardcode_paths(self):
        self._builder.unhardcode_paths(self._path)


class BuildHandle:

    def __init__(self, builder, distfiles):
        self._builder = builder
        self._distfiles = distfiles

    def archive(self, objects):
        return FileHandle(self._builder,
                          self._builder.archive(obj._path for obj in objects))

    def distfile(self, index=0):
        # Extract the distfile.
        distfile = self._distfiles[index]
        extractdir = self._builder.get_new_directory()
        subprocess.check_call(['tar', '-xC', extractdir, '-f',
                               distfile.tarball()])

        # Remove leading directory names.
        while True:
            entries = os.listdir(extractdir)
            if len(entries) != 1:
                break
            subdir = os.path.join(extractdir, entries[0])
            if not os.path.isdir(subdir):
                break
            extractdir = subdir

        # Apply patches.
        for patch in distfile.patches():
            with open(patch) as f:
                subprocess.check_call(
                    ['patch', '-d', extractdir, '-tsp0'], stdin=f)

        # Delete .orig files that patch leaves behind.
        for dirname, filename in util.walk_files(extractdir):
            if filename.endswith('.orig'):
                os.unlink(os.path.join(dirname, filename))
        return FileHandle(self._builder, extractdir)

    def prefix(self):
        return self._builder.get_prefix()


class Builder:

    def __init__(self, prefix):
        self._sequence_number = 0
        self._prefix = prefix
        self._builddir = os.path.join(config.DIR_BUILDROOT, 'build')

    def get_prefix(self):
        return self._prefix

    def get_new_archive(self):
        path = os.path.join(self._builddir, 'lib%d.a' % self._sequence_number)
        util.make_parent_dir(path)
        self._sequence_number += 1
        return path

    def get_new_directory(self):
        path = os.path.join(self._builddir, str(self._sequence_number))
        util.make_dir(path)
        self._sequence_number += 1
        return path


class PackageBuilder(Builder):

    def __init__(self, install_directory, arch):
        super(PackageBuilder, self).__init__('/nonexistent')
        self._install_directory = install_directory
        self._arch = arch

        self._bindir = os.path.join(config.DIR_BUILDROOT, 'bin')
        self._localbase = os.path.join(config.DIR_BUILDROOT, self._arch)
        self._cflags = ['-O2', '-fstack-protector-strong',
                        '-Werror=implicit-function-declaration']

    def _tool(self, name):
        return os.path.join(self._bindir, '%s-%s' % (self._arch, name))

    def archive(self, object_files):
        objs = sorted(object_files)
        output = self.get_new_archive()
        print('AR', output)
        subprocess.check_call([self._tool('ar'), '-rcs', output] + objs)
        return output

    def autoconf(self, builddir, script, args):
        self.run(builddir, [script, '--host=' + self._arch,
                            '--prefix=' + self.get_prefix()] + args)

    def cmake(self, builddir, sourcedir, args):
        self.run(builddir, [
            'cmake', sourcedir,
            '-DCMAKE_AR=' + self._tool('ar'),
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_FIND_ROOT_PATH=' + self._localbase,
            '-DCMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY',
            '-DCMAKE_FIND_ROOT_PATH_MODE_LIBRARY=ONLY',
            '-DCMAKE_FIND_ROOT_PATH_MODE_PROGRAM=NEVER',
            '-DCMAKE_INSTALL_PREFIX=' + self.get_prefix(),
            '-DCMAKE_PREFIX_PATH=' + self._localbase,
            '-DCMAKE_RANLIB=' + self._tool('ranlib'),
            '-DCMAKE_SYSTEM_NAME=Generic',
            '-DCMAKE_SYSTEM_PROCESSOR=' + self._arch.split('-')[0]] + args)

    def compile(self, source, target, args):
        os.chdir(os.path.dirname(source))
        ext = os.path.splitext(source)[1]
        if ext in {'.c', '.S'}:
            print('CC', source)
            subprocess.check_call(
                [self._tool('cc')] + self._cflags + args +
                ['-c', '-o', target, source])
        elif ext == '.cpp':
            print('CXX', source)
            subprocess.check_call(
                [self._tool('c++')] + self._cflags + args +
                ['-c', '-o', target, source])
        else:
            raise Exception('Unknown file extension: %s' % ext)

    def _unhardcode(self, source, target):
        with open(source, 'r') as f:
            contents = f.read()
        contents = (contents
                    .replace(self.get_prefix(), '%%PREFIX%%')
                    .replace(self._localbase, '%%PREFIX%%'))
        with open(target, 'w') as f:
            f.write(contents)

    def unhardcode_paths(self, path):
        self._unhardcode(path, path + '.template')
        shutil.copymode(path, path + '.template')
        os.unlink(path)

    def install(self, source, target):
        print('INSTALL', source, '->', target)
        target = os.path.join(self._install_directory, target)
        for source_file, target_file in util.walk_files_concurrently(
                source, target):
            util.make_parent_dir(target_file)
            ext = os.path.splitext(source_file)[1]
            if ext in {'.la', '.pc'}:
                # Remove references to the installation prefix and the localbase
                # directory from libtool archives and pkg-config files.
                self._unhardcode(source_file, target_file + '.template')
            else:
                # Copy other files literally.
                util.copy_file(source_file, target_file, False)

    def run(self, cwd, command):
        _chdir(cwd)
        subprocess.check_call([
            'env', '-i',
            'AR=' + self._tool('ar'),
            'CC=' + self._tool('cc'),
            'CXX=' + self._tool('c++'),
            'CFLAGS=' + ' '.join(self._cflags),
            'NM=' + self._tool('nm'),
            'OBJDUMP=' + self._tool('objdump'),
            'PATH=%s:/bin:/sbin:/usr/bin:/usr/sbin' % self._bindir,
            'PKG_CONFIG_LIBDIR=' +
            os.path.join(self._localbase, 'lib/pkgconfig'),
            'RANLIB=' + self._tool('ranlib'),
            'STRIP=' + self._tool('strip')] + command)


class HostPackageBuilder(Builder):

    def __init__(self, install_directory):
        super(HostPackageBuilder, self).__init__(config.DIR_BUILDROOT)
        self._install_directory = install_directory

    def autoconf(self, builddir, script, args):
        self.run(builddir, [script, '--prefix=' + self.get_prefix()] + args)

    def cmake(self, builddir, sourcedir, args):
        self.run(builddir, [
            'cmake', sourcedir, '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=' + self.get_prefix()] + args)

    def install(self, source, target):
        print('INSTALL', source, '->', target)
        target = os.path.join(self._install_directory, target)
        for source_file, target_file in util.walk_files_concurrently(
                source, target):
            util.make_parent_dir(target_file)
            util.copy_file(source_file, target_file, False)

    def run(self, cwd, command):
        _chdir(cwd)
        subprocess.check_call(command)
