#!/usr/bin/env python3
# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

import os
import sys

from src import config
from src import util
from src.catalog import ArchLinuxCatalog, CygwinCatalog, DebianCatalog, FreeBSDCatalog, HomebrewCatalog, NetBSDCatalog, OpenBSDCatalog
from src.repository import Repository
from src.version import FullVersion

# Locations relative to the source tree.
DIR_ROOT = os.getcwd()
DIR_DISTFILES = os.path.join(DIR_ROOT, '_obj/distfiles')
DIR_INSTALL = os.path.join(DIR_ROOT, '_obj/install')
DIR_PACKAGES_ARCHLINUX = os.path.join(DIR_ROOT, '_obj/packages/archlinux')
DIR_PACKAGES_CYGWIN = os.path.join(DIR_ROOT, '_obj/packages/cygwin')
DIR_PACKAGES_DEBIAN = os.path.join(DIR_ROOT, '_obj/packages/debian')
DIR_PACKAGES_FREEBSD = os.path.join(DIR_ROOT, '_obj/packages/freebsd')
DIR_PACKAGES_HOMEBREW = os.path.join(DIR_ROOT, '_obj/packages/homebrew')
DIR_PACKAGES_NETBSD = os.path.join(DIR_ROOT, '_obj/packages/netbsd')
DIR_PACKAGES_OPENBSD = os.path.join(DIR_ROOT, '_obj/packages/openbsd')
DIR_REPOSITORY = os.path.join(DIR_ROOT, 'packages')

# Parse all of the BUILD rules.
repo = Repository(DIR_INSTALL)
for filename in util.walk_files(DIR_REPOSITORY):
    if os.path.basename(filename) == 'BUILD':
        repo.add_build_file(filename, DIR_DISTFILES)
target_packages = repo.get_target_packages()

catalogs = {
    ArchLinuxCatalog(None, DIR_PACKAGES_ARCHLINUX),
    CygwinCatalog(None, DIR_PACKAGES_CYGWIN),
    DebianCatalog(None, DIR_PACKAGES_DEBIAN),
    FreeBSDCatalog(None, DIR_PACKAGES_FREEBSD),
    HomebrewCatalog(None, DIR_PACKAGES_HOMEBREW),
    NetBSDCatalog(None, DIR_PACKAGES_NETBSD),
    OpenBSDCatalog(None, DIR_PACKAGES_OPENBSD),
}


def build_package(package):
    version = FullVersion(version=package.get_version())
    for catalog in catalogs:
        catalog.insert(package, version, catalog.package(package, version))


if len(sys.argv) > 1:
    # Only build the packages provided on the command line.
    for name in set(sys.argv[1:]):
        for arch in config.ARCHITECTURES:
            build_package(target_packages[(name, arch)])
else:
    # Build all packages.
    for package in target_packages.values():
        build_package(package)

# When terminating successfully, remove the build directory. It will
# only contain temporary files that were used to generate the last
# package.
util.remove(config.DIR_BUILDROOT)
