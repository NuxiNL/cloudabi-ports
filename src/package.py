import os
import shutil

from . import config
from . import util
from .builder import BuildHandle, HostBuilder, TargetBuilder


class Package:

    def __init__(
            self,
            install_directory,
            name,
            version,
            distfiles,
            build_cmd):
        self._install_directory = install_directory
        self._name = name
        self._version = version
        self._distfiles = distfiles
        self._build_cmd = build_cmd

    def build(self):
        # Skip this package if it has been built already.
        if not self._build_cmd or os.path.isdir(self._install_directory):
            return

        # Ensure that all dependencies have been built.
        builddeps = self.get_build_dependencies()
        for dep in builddeps:
            dep.build()

        # Create a clean building directory and extract all of the
        # dependencies into it.
        print('BUILD', self._name)
        try:
            util.remove(config.DIR_BUILDROOT)
        except FileNotFoundError:
            pass
        for dep in builddeps:
            dep.extract_into_buildroot()

        # Perform the build.
        self._build_cmd(
            BuildHandle(
                self.get_builder(
                    self._install_directory),
                self._name,
                self._version,
                self._distfiles))

    def extract(self, path):
        for source_file, target_file in util.walk_files_concurrently(
                self._install_directory, path):
            util.make_parent_dir(target_file)
            if target_file.endswith('.template'):
                # File is a template. Expand %%PREFIX%% tags.
                target_file = target_file[:-9]
                with open(source_file, 'r') as f:
                    contents = f.read()
                contents = contents.replace('%%PREFIX%%', path)
                with open(target_file, 'w') as f:
                    f.write(contents)
                shutil.copymode(source_file, target_file)
            else:
                # Regular file. Copy it over literally.
                util.copy_file(source_file, target_file, False)


class TargetPackage(Package):

    def __init__(
            self,
            install_directory,
            arch,
            name,
            version,
            homepage,
            maintainer,
            host_depends,
            lib_depends,
            distfiles,
            build_cmd=None):
        super(
            TargetPackage,
            self).__init__(
            install_directory,
            name, version,
            distfiles,
            build_cmd)
        self._arch = arch

        # Compute the set of transitive build dependencies.
        self._build_depends = host_depends | lib_depends
        for dep in self._build_depends.copy():
            self._build_depends |= dep.get_build_dependencies()

    def extract_into_buildroot(self):
        # Target packages are extracted into <buildroot>/<arch>.
        self.extract(os.path.join(config.DIR_BUILDROOT, self._arch))

    def get_build_dependencies(self):
        return self._build_depends

    def get_builder(self, install_directory):
        return TargetBuilder(install_directory, self._arch)


class HostPackage(Package):

    def __init__(
            self,
            install_directory,
            name,
            version,
            homepage,
            maintainer,
            distfiles,
            build_cmd):
        super(HostPackage, self).__init__(install_directory, name,
                                          version, distfiles, build_cmd)

    def extract_into_buildroot(self):
        # Host packages are extracted into <buildroot>.
        self.extract(config.DIR_BUILDROOT)

    @staticmethod
    def get_build_dependencies():
        # Host packages have no build dependencies.
        return set()

    @staticmethod
    def get_builder(install_directory):
        return HostBuilder(install_directory)
