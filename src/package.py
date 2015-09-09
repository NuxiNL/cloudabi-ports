import os
import shutil
import stat
import subprocess

from . import config
from . import util
from .builder import BuildHandle, HostBuilder, TargetBuilder


def _empty_dir(self):
    # TODO(ed): This should not delete the actual directory.
    try:
        util.remove(config.DIR_BUILDROOT)
    except FileNotFoundError:
        pass


class HostPackage:

    def __init__(
            self,
            install_directory,
            name,
            version,
            homepage,
            maintainer,
            lib_depends,
            distfiles,
            build_cmd):
        self._install_directory = install_directory
        self._name = name
        self._version = version
        self._distfiles = distfiles
        self._build_cmd = build_cmd

        # Compute the set of transitive library dependencies.
        self._lib_depends = set()
        for dep in lib_depends:
            self._lib_depends.add(dep)
            self._lib_depends |= dep._lib_depends

    def _prepare_buildroot(self):
        # Ensure that all dependencies have been built.
        for dep in self._lib_depends:
            dep.build()

        # Install dependencies into an empty buildroot.
        _empty_dir(config.DIR_BUILDROOT)
        for dep in self._lib_depends:
            dep.extract()

    def build(self):
        # Skip this package if it has been built already.
        if os.path.isdir(self._install_directory):
            return

        # Perform the build inside an empty buildroot.
        self._prepare_buildroot()
        print('BUILD', self._name)
        self._build_cmd(
            BuildHandle(
                HostBuilder(
                    self._install_directory),
                self._name,
                self._version,
                self._distfiles))

    def extract(self):
        # Copy files literally.
        for source_file, target_file in util.walk_files_concurrently(
                self._install_directory, config.DIR_BUILDROOT):
            util.make_parent_dir(target_file)
            util.copy_file(source_file, target_file, False)


class TargetPackage:

    def __init__(
            self,
            install_directory,
            arch,
            name,
            version,
            homepage,
            maintainer,
            host_packages,
            lib_depends,
            build_cmd,
            distfiles):
        self._install_directory = install_directory
        self._arch = arch
        self._name = name
        self._version = version
        self._homepage = homepage
        self._maintainer = maintainer
        self._host_packages = host_packages
        self._build_cmd = build_cmd
        self._distfiles = distfiles

        # Compute the set of transitive library dependencies.
        self._lib_depends = set()
        for dep in lib_depends:
            if dep._build_cmd:
                self._lib_depends.add(dep)
            self._lib_depends |= dep._lib_depends

        # Debian package naming scheme.
        self._debian_name = '%s-%s' % (arch.replace('_', '-'), name)

    @staticmethod
    def _get_suggested_mode(path):
        mode = os.lstat(path).st_mode
        if stat.S_ISLNK(mode):
            # Symbolic links.
            return 0o777
        elif stat.S_ISDIR(mode) or (mode & 0o111) != 0:
            # Directories and executable files.
            return 0o555
        else:
            # Non-executable files.
            return 0o444

    def _prepare_buildroot(self, host_depends, lib_depends):
        # Ensure that all dependencies have been built.
        for dep in host_depends:
            package = self._host_packages[dep]
            package.build()
            for depdep in package._lib_depends:
                depdep.build()
        for dep in lib_depends:
            dep.build()

        # Install dependencies into an empty buildroot.
        _empty_dir(config.DIR_BUILDROOT)
        for dep in host_depends:
            package = self._host_packages[dep]
            package.extract()
            for depdep in package._lib_depends:
                depdep.extract()
        prefix = os.path.join(config.DIR_BUILDROOT, self._arch)
        for dep in lib_depends:
            dep.extract(prefix, prefix)

    def build(self):
        # Skip this package if it has been built already.
        if not self._build_cmd or os.path.isdir(self._install_directory):
            return

        # Perform the build inside a buildroot with its dependencies
        # installed in place.
        self._prepare_buildroot(set([
            'binutils', 'cmake', 'llvm', 'make', 'pkgconf',
        ]), self._lib_depends)
        print('BUILD', self._name)
        self._build_cmd(
            BuildHandle(
                TargetBuilder(
                    self._install_directory,
                    self._arch),
                self._name,
                self._version,
                self._distfiles))

    def create_debian_package(self):
        self.build()
        self._prepare_buildroot(set(['binutils', 'libarchive']), set())
        print('PKG', self._name, 'Debian')

        rootdir = config.DIR_BUILDROOT
        debian_binary = os.path.join(rootdir, 'debian-binary')
        controldir = os.path.join(rootdir, 'control')
        datadir = os.path.join(rootdir, 'data')

        # Create 'debian-binary' file.
        with open(debian_binary, 'w') as f:
            f.write('2.0\n')

        def tar(directory):
            # Reset permissions to sane values.
            for root, dirs, files in os.walk(directory):
                os.lchmod(root, 0o555)
                for filename in files:
                    path = os.path.join(root, filename)
                    os.lchmod(path, self._get_suggested_mode(path))

            # Create tarball.
            subprocess.check_call([
                os.path.join(rootdir, 'bin/bsdtar'),
                '-cJf', directory + '.tar.xz',
                '-C', directory,
                '.',
            ])

        # Create 'control.tar.gz' tarball that contains the control file.
        util.make_dir(controldir)
        with open(os.path.join(controldir, 'control'), 'w') as f:
            f.write(
                'Package: %(debian_name)s\n'
                'Version: %(version)s\n'
                'Architecture: all\n'
                'Maintainer: %(maintainer)s\n'
                'Description: %(name)s for %(arch)s\n'
                'Homepage: %(homepage)s\n' % {
                    'arch': self._arch,
                    'homepage': self._homepage,
                    'maintainer': self._maintainer,
                    'name': self._name,
                    'debian_name': self._debian_name,
                    'version': self._version
                })
            if self._lib_depends:
                f.write(
                    'Depends: %s\n' % ', '.join(sorted(
                        dep._debian_name for dep in self._lib_depends)))
        tar(controldir)

        # Create 'data.tar.xz' tarball that contains the files that need
        # to be installed by the package.
        prefix = os.path.join('/usr', self._arch)
        util.make_dir(datadir)
        self.extract(os.path.join(datadir, prefix[1:]), prefix)
        tar(datadir)

        path = os.path.join(
            rootdir, '%s_%s_all.deb' % (self._debian_name, self._version))
        subprocess.check_call([
            os.path.join(rootdir, 'bin/x86_64-unknown-cloudabi-ar'),
            '-rc', path,
            debian_binary, controldir + '.tar.xz', datadir + '.tar.xz',
        ])
        return path

    def create_freebsd_package(self):
        # Install just a copy of FreeBSD's pkg(8) into the buildroot,
        # which we can call into to create the package.
        self.build()
        self._prepare_buildroot(set(['pkg']), set())
        print('PKG', self._name, 'FreeBSD')

        # The package needs to be installed in /usr/local/<arch> on the
        # FreeBSD system.
        prefix = os.path.join('/usr/local', self._arch)
        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        filesdir = os.path.join(installdir, prefix[1:])
        self.extract(filesdir, prefix)

        # Create a manifest file.
        util.make_dir(installdir)
        with open(os.path.join(installdir, '+MANIFEST'), 'w') as f:
            # Preamble.
            f.write(
                'name: %(arch)s-%(name)s\n'
                'version: \"%(version)s\"\n'
                'origin: devel/%(arch)s-%(name)s\n'
                'comment: %(name)s for %(arch)s\n'
                'www: %(homepage)s\n'
                'maintainer: %(maintainer)s\n'
                'prefix: /usr/local\n'
                'desc: %(name)s for %(arch)s\n'
                'abi: FreeBSD:*\n'
                'arch: freebsd:*\n' % {
                    'arch': self._arch,
                    'homepage': self._homepage,
                    'maintainer': self._maintainer,
                    'name': self._name,
                    'version': self._version
                })

            # Dependencies.
            f.write('deps: {\n')
            for dep in sorted('%s-%s' % (pkg._arch, pkg._name)
                              for pkg in self._lib_depends):
                f.write(
                    '  \"%s\": {origin: devel/%s, version: 0}\n' %
                    (dep, dep))
            f.write('}\n')

            # Create entry for every file.
            f.write('files: {\n')
            for path in sorted(util.walk_files(filesdir)):
                f.write(
                    '  \"/%s\": { perm: 0%o }' % (
                        os.path.relpath(path, installdir),
                        self._get_suggested_mode(path)))
            f.write('}\n')

        # Create the package.
        subprocess.check_call([
            os.path.join(config.DIR_BUILDROOT, 'sbin/pkg'),
            'create',
            '-r', installdir,
            '-m', installdir,
            '-o', config.DIR_BUILDROOT,
        ])
        return os.path.join(
            config.DIR_BUILDROOT, '%s-%s-%s.txz' %
            (self._arch, self._name, self._version))

    def extract(self, path, expandpath):
        for source_file, target_file in util.walk_files_concurrently(
                self._install_directory, path):
            util.make_parent_dir(target_file)
            if target_file.endswith('.template'):
                # File is a template. Expand %%PREFIX%% tags.
                target_file = target_file[:-9]
                with open(source_file, 'r') as f:
                    contents = f.read()
                contents = contents.replace('%%PREFIX%%', expandpath)
                with open(target_file, 'w') as f:
                    f.write(contents)
                shutil.copymode(source_file, target_file)
            else:
                # Regular file. Copy it over literally.
                util.copy_file(source_file, target_file, False)
