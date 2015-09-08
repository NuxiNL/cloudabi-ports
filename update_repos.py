#!/usr/bin/env python3

import os
import subprocess

from src import util
from src.repository import Repository

# TODO(ed): This script overwrites existing packages, without bumping
# revision or Epoch numbers. This should be fixed.
# TODO(ed): This script should build everything package twice, to
# double-check that the build is reproducible.

# Public location where package distfiles are stored.
DIR_DISTFILES = '/usr/local/www/nuxi.nl/public/distfiles/third_party'

# Temporary directory where intermediate build results are stored.
DIR_TMP = '/usr/local/www/nuxi.nl/repo.tmp'

# Final location of the FreeBSD packages.
DIR_FREEBSD_REPO = '/usr/local/www/nuxi.nl/public/distfiles/cloudabi-ports/freebsd'

# Zap the old temporary directory.
try:
    util.remove(DIR_TMP)
except FileNotFoundError:
    pass

# Parse all of the BUILD rules.
repo = Repository(os.path.join(DIR_TMP, 'install'))
for filename in util.walk_files(os.path.join(os.getcwd(), 'packages')):
    if os.path.basename(filename) == 'BUILD':
        repo.add_build_file(filename, DIR_DISTFILES)
target_packages = repo.get_target_packages()

# Build all packages.
freebsd_repo = os.path.join(DIR_TMP, 'freebsd')
for name, arch in target_packages:
    path = target_packages[(name, arch)].create_freebsd_package()
    target = os.path.join(freebsd_repo, os.path.basename(path))
    util.make_parent_dir(target)
    os.rename(path, target)

# Sign the repositories.
# TODO(ed): Use the 'pkg' binary from the build process, instead of
# using the one from the host system.
# TODO(ed): Sign the repository.
subprocess.check_call(['pkg', 'repo', freebsd_repo])

# Exchange the old repositories with the new ones.
os.rename(DIR_FREEBSD_REPO, os.path.join(DIR_TMP, 'freebsd.old'))
os.rename(freebsd_repo, DIR_FREEBSD_REPO)

# Zap the temporary directory.
util.remove(DIR_TMP)
