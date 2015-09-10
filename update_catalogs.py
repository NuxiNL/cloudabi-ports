#!/usr/bin/env python3
# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.

import os

from src import util
from src.catalog import DebianCatalog, FreeBSDCatalog
from src.catalog_set import CatalogSet
from src.repository import Repository

# Public location where package distfiles are stored.
DIR_DISTFILES = '/usr/local/www/nuxi.nl/public/distfiles/third_party'

# Temporary directory where intermediate build results are stored.
DIR_TMP = '/usr/local/www/nuxi.nl/repo.tmp'

# Final location of the catalogs.
DIR_DEBIAN_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/debian'
DIR_FREEBSD_CATALOG = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/freebsd'

# Location of the catalog signing keys.
DEBIAN_PRIVATE_KEY = '31344B15'
FREEBSD_PRIVATE_KEY = '/home/edje/.cloudabi-ports-freebsd.key'

# Zap the old temporary directory.
util.remove_and_make_dir(DIR_TMP)

# Parse all of the BUILD rules.
# repo = Repository(os.path.join(DIR_TMP, 'install'))
repo = Repository(os.path.join(os.getcwd(), '_obj/install'))
for filename in util.walk_files(os.path.join(os.getcwd(), 'packages')):
    if os.path.basename(filename) == 'BUILD':
        repo.add_build_file(filename, DIR_DISTFILES)
target_packages = repo.get_target_packages()

# The catalogs that we want to create.
debian_path = os.path.join(DIR_TMP, 'debian')
debian_catalog = DebianCatalog(DIR_DEBIAN_CATALOG, debian_path)
freebsd_path = os.path.join(DIR_TMP, 'freebsd')
freebsd_catalog = FreeBSDCatalog(DIR_FREEBSD_CATALOG, freebsd_path)

# Build all packages.
catalog_set = CatalogSet({debian_catalog, freebsd_catalog})
for package in target_packages.values():
    catalog_set.package_and_insert(package, os.path.join(DIR_TMP, 'catalog'))

debian_catalog.finish(DEBIAN_PRIVATE_KEY)
freebsd_catalog.finish(FREEBSD_PRIVATE_KEY)

# Finish up and put the new catalogs in place.
os.rename(DIR_DEBIAN_CATALOG, os.path.join(DIR_TMP, 'debian.old'))
os.rename(debian_path, DIR_DEBIAN_CATALOG)
os.rename(DIR_FREEBSD_CATALOG, os.path.join(DIR_TMP, 'freebsd.old'))
os.rename(freebsd_path, DIR_FREEBSD_CATALOG)

# Zap the temporary directory.
util.remove(DIR_TMP)
