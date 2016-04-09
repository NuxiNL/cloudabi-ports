#!/usr/bin/env python3
# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

import os

from src import config
from src import util
from src.catalog import ArchLinuxCatalog, CygwinCatalog, DebianCatalog, FreeBSDCatalog, HomebrewCatalog, NetBSDCatalog, OpenBSDCatalog
from src.catalog_set import CatalogSet
from src.repository import Repository

# Public location where package distfiles are stored.
DIR_DISTFILES = '/usr/local/www/nuxi.nl/public/distfiles/third_party'

# Temporary directory where intermediate build results are stored.
DIR_TMP = '/usr/local/www/nuxi.nl/repo.tmp'

# Final location of the catalogs.
DIR_ARCHLINUX_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/archlinux'
DIR_CYGWIN_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/cygwin'
DIR_DEBIAN_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/debian'
DIR_FREEBSD_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/freebsd'
DIR_HOMEBREW_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/homebrew'
DIR_NETBSD_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/netbsd'
DIR_OPENBSD_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/openbsd'

# Location of the catalog signing keys.
ARCHLINUX_PRIVATE_KEY = '31344B15'
CYGWIN_PRIVATE_KEY = 'A4836F43'
DEBIAN_PRIVATE_KEY = '31344B15'
FREEBSD_PRIVATE_KEY = '/home/edje/.cloudabi-ports-freebsd.key'

# The Homebrew repository needs to know its own URL.
HOMEBREW_URL = 'https://nuxi.nl/distfiles/cloudabi-ports/homebrew/'

# Zap the old temporary directory.
util.remove_and_make_dir(DIR_TMP)

# Parse all of the BUILD rules.
repo = Repository(os.path.join(DIR_TMP, 'install'))
# repo = Repository(os.path.join(os.getcwd(), '_obj/install'))
for filename in util.walk_files(os.path.join(os.getcwd(), 'packages')):
    if os.path.basename(filename) == 'BUILD':
        repo.add_build_file(filename, DIR_DISTFILES)
target_packages = repo.get_target_packages()

# The catalogs that we want to create.
archlinux_path = os.path.join(DIR_TMP, 'archlinux')
archlinux_catalog = ArchLinuxCatalog(DIR_ARCHLINUX_CATALOG, archlinux_path)
cygwin_path = os.path.join(DIR_TMP, 'cygwin')
cygwin_catalog = CygwinCatalog(DIR_CYGWIN_CATALOG, cygwin_path)
debian_path = os.path.join(DIR_TMP, 'debian')
debian_catalog = DebianCatalog(DIR_DEBIAN_CATALOG, debian_path)
freebsd_path = os.path.join(DIR_TMP, 'freebsd')
freebsd_catalog = FreeBSDCatalog(DIR_FREEBSD_CATALOG, freebsd_path)
homebrew_path = os.path.join(DIR_TMP, 'homebrew')
homebrew_catalog = HomebrewCatalog(DIR_HOMEBREW_CATALOG, homebrew_path,
                                   HOMEBREW_URL)
netbsd_path = os.path.join(DIR_TMP, 'netbsd')
netbsd_catalog = NetBSDCatalog(DIR_NETBSD_CATALOG, netbsd_path)
openbsd_path = os.path.join(DIR_TMP, 'openbsd')
openbsd_catalog = OpenBSDCatalog(DIR_OPENBSD_CATALOG, openbsd_path)

# Build all packages.
catalog_set = CatalogSet({
    archlinux_catalog, cygwin_catalog, debian_catalog, freebsd_catalog,
    homebrew_catalog, netbsd_catalog, openbsd_catalog,
})
for package in target_packages.values():
    catalog_set.package_and_insert(package, os.path.join(DIR_TMP, 'catalog'))

archlinux_catalog.finish(ARCHLINUX_PRIVATE_KEY)
cygwin_catalog.finish(CYGWIN_PRIVATE_KEY)
debian_catalog.finish(DEBIAN_PRIVATE_KEY)
freebsd_catalog.finish(FREEBSD_PRIVATE_KEY)
homebrew_catalog.finish()

# Finish up and put the new catalogs in place.
os.rename(DIR_ARCHLINUX_CATALOG, os.path.join(DIR_TMP, 'archlinux.old'))
os.rename(archlinux_path, DIR_ARCHLINUX_CATALOG)
os.rename(DIR_CYGWIN_CATALOG, os.path.join(DIR_TMP, 'cygwin.old'))
os.rename(cygwin_path, DIR_CYGWIN_CATALOG)
os.rename(DIR_DEBIAN_CATALOG, os.path.join(DIR_TMP, 'debian.old'))
os.rename(debian_path, DIR_DEBIAN_CATALOG)
os.rename(DIR_FREEBSD_CATALOG, os.path.join(DIR_TMP, 'freebsd.old'))
os.rename(freebsd_path, DIR_FREEBSD_CATALOG)
os.rename(DIR_HOMEBREW_CATALOG, os.path.join(DIR_TMP, 'homebrew.old'))
os.rename(homebrew_path, DIR_HOMEBREW_CATALOG)
os.rename(DIR_NETBSD_CATALOG, os.path.join(DIR_TMP, 'netbsd.old'))
os.rename(netbsd_path, DIR_NETBSD_CATALOG)
os.rename(DIR_OPENBSD_CATALOG, os.path.join(DIR_TMP, 'openbsd.old'))
os.rename(openbsd_path, DIR_OPENBSD_CATALOG)

# Zap the temporary directories.
util.remove(config.DIR_BUILDROOT)
util.remove(DIR_TMP)
