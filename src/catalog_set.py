import os

from . import util
from .version import FullVersion


class CatalogSet:

    def __init__(self, catalogs):
        self._catalogs = catalogs

    def _determine_start_version(self, package):
        version = FullVersion(0, package.get_version(), 0)
        for catalog in self._catalogs:
            latest_version = catalog.lookup_latest_version(package)
            if latest_version and latest_version > version:
                version = latest_version.bump_version(package.get_version())
        return version

    def _build_at_version(self, package, version, tmpdir):
        # Round 1: Build the packages.
        util.remove_and_make_dir(tmpdir)
        do_rebuild = []
        do_preserve = []
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
                new = os.path.join(tmpdir, str(len(do_preserve)))
                os.rename(path, new)
                do_rebuild.append(catalog)

        # Round 2: Do a rebuild to ensure that the build is
        # deterministic. Two successive builds should yield the same
        # packages.
        if do_rebuild:
            package.clean()
            for idx, catalog in do_rebuild:
                path1 = os.path.join(tmpdir, str(idx))
                path2 = catalog.package(package, version)
                if not util.file_contents_equal(path1, path2):
                    raise Exception(
                        'Package %s is not deterministic, as %s and %s are not equal' %
                        (package, path1, path2))
                catalog.insert(package, version, path1)
        for catalog, path in do_preserve:
            catalog.insert(package, version, path)
        return True

    def package_and_insert(self, package, tmpdir):
        version = self._determine_start_version(package)
        while not self._build_at_version(package, version, tmpdir):
            version = version.bump_revision()
