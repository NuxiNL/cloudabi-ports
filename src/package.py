import os
import shutil

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
            distfiles,
            build_cmd):
        self._install_directory = install_directory
        self._name = name
        self._version = version
        self._distfiles = distfiles
        self._build_cmd = build_cmd

    def build(self):
        # Skip this package if it has been built already.
        if os.path.isdir(self._install_directory):
            return

        # Perform the build inside an empty buildroot.
        _empty_dir(config.DIR_BUILDROOT)
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
        self._host_packages = host_packages
        self._lib_depends = lib_depends
        self._build_cmd = build_cmd
        self._distfiles = distfiles

        # Compute the set of transitive library dependencies.
        self._transitive_lib_depends = set()
        for dep in self._lib_depends:
            self._transitive_lib_depends.add(dep)
            self._transitive_lib_depends |= dep._transitive_lib_depends

    def _prepare_buildroot(self, host_depends, lib_depends):
        # Ensure that all dependencies have been built.
        for dep in host_depends:
            self._host_packages[dep].build()
        for dep in lib_depends:
            dep.build()

        # Install dependencies into an empty buildroot.
        _empty_dir(config.DIR_BUILDROOT)
        for dep in host_depends:
            self._host_packages[dep].extract()
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
        ]), self._transitive_lib_depends)
        print('BUILD', self._name)
        self._build_cmd(
            BuildHandle(
                TargetBuilder(
                    self._install_directory,
                    self._arch),
                self._name,
                self._version,
                self._distfiles))

    def create_freebsd_package(self, path):
        # Install just a copy of FreeBSD's pkg(8) into the buildroot,
        # which we can call into to create the package.
        self.build()
        self._prepare_buildroot(set(['pkg']), set())

        # The package needs to be installed in /usr/local/<arch> on the
        # FreeBSD system.
        prefix = os.path.join('/usr/local', self._arch)
        installdir = os.path.join(config.DIR_BUILDROOT, 'install', prefix[1:])
        self.extract(installdir, prefix)

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
