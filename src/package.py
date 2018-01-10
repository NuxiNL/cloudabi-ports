# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import logging
import os
import shutil
import sys

from . import config
from . import util
from .builder import BuildDirectory, BuildHandle, HostBuilder, TargetBuilder

from src.distfile import Distfile
from src.version import SimpleVersion
from typing import AbstractSet, Callable, Dict, Optional, Set
log = logging.getLogger(__name__)


class HostPackage:
    def __init__(
            self, install_directory: str, name: str, version: SimpleVersion,
            homepage: str, build_depends: Set['HostPackage'],
            lib_depends: Set['HostPackage'], distfiles: Dict[str, Distfile],
            build_cmd: Callable[[BuildHandle], None],
            resource_directory: str) -> None:
        self._install_directory = install_directory
        self._name = name
        self._version = version
        self._distfiles = distfiles
        self._build_cmd = build_cmd
        self._resource_directory = resource_directory

        # Compute the set of transitive build dependencies.
        self._build_depends = set()  # type: Set['HostPackage']
        for dep in build_depends:
            self._build_depends.add(dep)
            self._build_depends |= dep._lib_depends

        # Compute the set of transitive library dependencies.
        self._lib_depends = set()  # type: Set['HostPackage']
        for dep in lib_depends:
            self._lib_depends.add(dep)
            self._lib_depends |= dep._lib_depends

    def _initialize_buildroot(self) -> None:
        # Ensure that all dependencies have been built.
        deps = self._build_depends | self._lib_depends
        for dep in deps:
            dep.build()

        # Install dependencies into an empty buildroot.
        util.remove_and_make_dir(config.DIR_BUILDROOT)
        for dep in deps:
            dep.extract()

    def build(self) -> None:
        # Skip this package if it has been built already.
        if os.path.isdir(self._install_directory):
            return

        # Perform the build inside an empty buildroot.
        self._initialize_buildroot()
        log.info('BUILD %s', self._name)
        self._build_cmd(
            BuildHandle(
                HostBuilder(BuildDirectory(),
                            self._install_directory), self._name,
                self._version, self._distfiles, self._resource_directory))

    def extract(self) -> None:
        # Copy files literally.
        for source_file, target_file in util.walk_files_concurrently(
                self._install_directory, config.DIR_BUILDROOT):
            util.make_parent_dir(target_file)
            util.copy_file(source_file, target_file, False)


class TargetPackage:
    def __init__(self,
                 install_directory: str,
                 arch: str,
                 name: str,
                 version: SimpleVersion,
                 homepage: str,
                 host_packages: Dict[str, HostPackage],
                 lib_depends: Set['TargetPackage'],
                 build_cmd: Optional[Callable],
                 distfiles: Dict[str, Distfile],
                 resource_directory: Optional[str],
                 replaces: AbstractSet[str] = frozenset()) -> None:
        self._install_directory = install_directory
        self._arch = arch
        self._name = name
        self._version = version
        self._homepage = homepage
        self._host_packages = host_packages
        self._build_cmd = build_cmd
        self._distfiles = distfiles
        self._resource_directory = resource_directory
        self._replaces = replaces

        # Compute the set of transitive library dependencies.
        self._lib_depends = set()  # type: Set['TargetPackage']
        for dep in lib_depends:
            if dep._build_cmd:
                self._lib_depends.add(dep)
            self._lib_depends |= dep._lib_depends

    def __str__(self):
        return '%s %s' % (self.get_freebsd_name(), self._version)

    def build(self) -> None:
        # Skip this package if it has been built already.
        if not self._build_cmd or os.path.isdir(self._install_directory):
            return

        # Perform the build inside a buildroot with its dependencies
        # installed in place.
        self.initialize_buildroot({
            'arpc', 'autoconf', 'automake', 'bash', 'bison', 'c-ares', 'cmake',
            'coreutils', 'diffutils', 'findutils', 'flex', 'gawk', 'gettext',
            'grep', 'grpc', 'help2man', 'libarchive', 'libtool', 'llvm', 'm4',
            'make', 'ninja', 'pkgconf', 'protobuf-cpp', 'sed', 'texinfo'
        }, self._lib_depends)
        log.info('BUILD %s %s', self._name, self._arch)
        self._build_cmd(
            BuildHandle(
                TargetBuilder(BuildDirectory(), self._install_directory,
                              self._arch), self._name, self._version,
                self._distfiles, self._resource_directory))

    def clean(self):
        util.remove(self._install_directory)

    def extract(self, path: str, expandpath: str) -> None:
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

    def get_arch(self) -> str:
        return self._arch

    def get_archlinux_name(self) -> str:
        return '%s-%s' % (self._arch, self._name)

    def get_cygwin_name(self) -> str:
        return '%s-%s' % (self._arch, self._name)

    def get_debian_name(self) -> str:
        return '%s-%s' % (self._arch.replace('_', '-'), self._name)

    def get_freebsd_name(self) -> str:
        return '%s-%s' % (self._arch, self._name)

    def get_homebrew_name(self) -> str:
        return '%s-%s' % (self._arch, self._name)

    def get_netbsd_name(self) -> str:
        return '%s-%s' % (self._arch, self._name)

    def get_openbsd_name(self) -> str:
        return '%s-%s' % (self._arch, self._name)

    def get_redhat_name(self) -> str:
        return '%s-%s' % (self._arch, self._name)

    def get_homepage(self) -> str:
        return self._homepage

    def get_lib_depends(self) -> Set['TargetPackage']:
        return self._lib_depends

    def get_replaces(self) -> AbstractSet[str]:
        return self._replaces

    def get_maintainer(self) -> str:
        return 'info@nuxi.nl'

    def get_name(self) -> str:
        return self._name

    def get_version(self) -> SimpleVersion:
        return self._version

    def initialize_buildroot(
            self,
            host_depends: Set[str],
            lib_depends: Set['TargetPackage'] = set()) -> None:
        # Ensure that all dependencies have been built.
        host_deps = set()  # type: Set[HostPackage]
        for dep_name in host_depends:
            package = self._host_packages[dep_name]
            host_deps.add(package)
            for depdep in package._lib_depends:
                host_deps.add(depdep)
        for dep in host_deps:
            dep.build()
        for ldep in lib_depends:
            ldep.build()

        # Install dependencies into an empty buildroot.
        util.remove_and_make_dir(config.DIR_BUILDROOT)
        for dep in host_deps:
            dep.extract()
        prefix = os.path.join(config.DIR_BUILDROOT, self._arch)
        for ldep in lib_depends:
            ldep.extract(prefix, prefix)

        # Also allow us to call into Python from within the buildroot.
        # TODO(ed): Should we add Python as a host package as well?
        os.symlink(config.PYTHON2,
                   os.path.join(config.DIR_BUILDROOT, 'bin/python2'))
        os.symlink(sys.executable,
                   os.path.join(config.DIR_BUILDROOT, 'bin/python'))
        os.symlink(sys.executable,
                   os.path.join(config.DIR_BUILDROOT, 'bin/python3'))
