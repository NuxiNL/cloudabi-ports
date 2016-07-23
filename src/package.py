# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

import logging
import os
import shutil
import stat
import subprocess

from . import config
from . import util
from .builder import BuildDirectory, BuildHandle, HostBuilder, TargetBuilder

log = logging.getLogger(__name__)

class HostPackage:

    def __init__(self, install_directory, name, version, homepage,
                 maintainer, build_depends, lib_depends, distfiles,
                 build_cmd, resource_directory):
        self._install_directory = install_directory
        self._name = name
        self._version = version
        self._distfiles = distfiles
        self._build_cmd = build_cmd
        self._resource_directory = resource_directory

        # Compute the set of transitive build dependencies.
        self._build_depends = set()
        for dep in build_depends:
            self._build_depends.add(dep)
            self._build_depends |= dep._lib_depends

        # Compute the set of transitive library dependencies.
        self._lib_depends = set()
        for dep in lib_depends:
            self._lib_depends.add(dep)
            self._lib_depends |= dep._lib_depends

    def _initialize_buildroot(self):
        # Ensure that all dependencies have been built.
        deps = self._build_depends | self._lib_depends
        for dep in deps:
            dep.build()

        # Install dependencies into an empty buildroot.
        util.remove_and_make_dir(config.DIR_BUILDROOT)
        for dep in deps:
            dep.extract()

    def build(self):
        # Skip this package if it has been built already.
        if os.path.isdir(self._install_directory):
            return

        # Perform the build inside an empty buildroot.
        self._initialize_buildroot()
        log.info('BUILD %s', self._name)
        self._build_cmd(
            BuildHandle(
                HostBuilder(BuildDirectory(), self._install_directory),
                self._name, self._version, self._distfiles,
                self._resource_directory))

    def extract(self):
        # Copy files literally.
        for source_file, target_file in util.walk_files_concurrently(
                self._install_directory, config.DIR_BUILDROOT):
            util.make_parent_dir(target_file)
            util.copy_file(source_file, target_file, False)


class TargetPackage:

    def __init__(self, install_directory, arch, name, version, homepage,
                 maintainer, host_packages, lib_depends, build_cmd,
                 distfiles, resource_directory):
        self._install_directory = install_directory
        self._arch = arch
        self._name = name
        self._version = version
        self._homepage = homepage
        self._maintainer = maintainer
        self._host_packages = host_packages
        self._build_cmd = build_cmd
        self._distfiles = distfiles
        self._resource_directory = resource_directory

        # Compute the set of transitive library dependencies.
        self._lib_depends = set()
        for dep in lib_depends:
            if dep._build_cmd:
                self._lib_depends.add(dep)
            self._lib_depends |= dep._lib_depends

    def __str__(self):
        return '%s %s' % (self.get_freebsd_name(), self._version)

    def build(self):
        # Skip this package if it has been built already.
        if not self._build_cmd or os.path.isdir(self._install_directory):
            return

        # Perform the build inside a buildroot with its dependencies
        # installed in place.
        self.initialize_buildroot({
            'autoconf', 'automake', 'bash', 'bison', 'cmake',
            'coreutils', 'diffutils', 'findutils', 'flex', 'gawk',
            'gettext', 'grep', 'help2man', 'libarchive', 'libtool',
            'llvm', 'm4', 'make', 'ninja', 'pkgconf', 'sed', 'texinfo',
        }, self._lib_depends)
        log.info('BUILD %s', self._name)
        self._build_cmd(
            BuildHandle(
                TargetBuilder(BuildDirectory(),
                              self._install_directory, self._arch),
                self._name, self._version, self._distfiles,
                self._resource_directory))

    def clean(self):
        util.remove(self._install_directory)

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

    def get_arch(self):
        return self._arch

    def get_archlinux_name(self):
        return '%s-%s' % (self._arch, self._name)

    def get_cygwin_name(self):
        return '%s-%s' % (self._arch, self._name)

    def get_debian_name(self):
        return '%s-%s' % (self._arch.replace('_', '-'), self._name)

    def get_freebsd_name(self):
        return '%s-%s' % (self._arch, self._name)

    def get_homebrew_name(self):
        return '%s-%s' % (self._arch, self._name)

    def get_netbsd_name(self):
        return '%s-%s' % (self._arch, self._name)

    def get_openbsd_name(self):
        return '%s-%s' % (self._arch, self._name)

    def get_redhat_name(self):
        return '%s-%s' % (self._arch, self._name)

    def get_homepage(self):
        return self._homepage

    def get_lib_depends(self):
        return self._lib_depends

    def get_maintainer(self):
        return self._maintainer

    def get_name(self):
        return self._name

    def get_version(self):
        return self._version

    def initialize_buildroot(self, host_depends, lib_depends=set()):
        # Ensure that all dependencies have been built.
        host_deps = set()
        for dep in host_depends:
            package = self._host_packages[dep]
            host_deps.add(package)
            for depdep in package._lib_depends:
                host_deps.add(depdep)
        for dep in host_deps:
            dep.build()
        for dep in lib_depends:
            dep.build()

        # Install dependencies into an empty buildroot.
        util.remove_and_make_dir(config.DIR_BUILDROOT)
        for dep in host_deps:
            dep.extract()
        prefix = os.path.join(config.DIR_BUILDROOT, self._arch)
        for dep in lib_depends:
            dep.extract(prefix, prefix)
