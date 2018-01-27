# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import os
from typing import List, Set, Tuple

from . import util
from .version import FullVersion
from .catalog import Catalog
from .package import TargetPackage


class CatalogSet:
    def __init__(self, catalogs: Set[Catalog]) -> None:
        self._catalogs = catalogs

    def _build_at_version(self, package: TargetPackage, version: FullVersion,
                          tmpdir: str) -> bool:
        # Round 1: Build the packages.
        util.remove_and_make_dir(tmpdir)
        do_rebuild = []  # type: List[Catalog]
        do_preserve = []  # type: List[Tuple[Catalog, str]]
        List, Tuple  # for tools that don't see comments
        for catalog in self._catalogs:
            path = catalog.package(package, version)
            existing = catalog.lookup_at_version(package, version)
            if existing:
                if util.file_contents_equal(path, existing):
                    # It is still equal to the existing package. Discard
                    # this package and keep the old file.
                    do_preserve.append((catalog, existing))
                else:
                    # It is unequal. We should bump the revision to
                    # indicate the change.
                    return False
            else:
                # A new package. Keep it.
                new = os.path.join(tmpdir, str(len(do_rebuild)))
                os.rename(path, new)
                do_rebuild.append(catalog)

        # Round 2: Do a rebuild to ensure that the build is
        # deterministic. Two successive builds should yield the same
        # packages.
        if do_rebuild:
            package.clean()
            for idx, catalog in enumerate(do_rebuild):
                path1 = os.path.join(tmpdir, str(idx))
                path2 = catalog.package(package, version)
                if not util.file_contents_equal(path1, path2):
                    raise Exception(
                        'Package %s is not deterministic, as %s and %s are not equal'
                        % (package, path1, path2))
                catalog.insert(package, version, path1)
        for catalog, path in do_preserve:
            catalog.insert(package, version, path)
        return True

    def package_and_insert(self, package: TargetPackage, tmpdir: str) -> None:
        # Scan the existing catalogs to determine the Epoch and revision
        # numbers of the latest version of the package. At this version
        # we need to start building.
        version = FullVersion(version=package.get_version())
        for catalog in self._catalogs:
            version.bump_epoch_revision(catalog.lookup_latest_version(package))

        # Increment the revision if we rebuild a package and the
        # checksum has changed.
        while not self._build_at_version(package, version, tmpdir):
            version = version.bump_revision()
