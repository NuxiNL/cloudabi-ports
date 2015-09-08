#!/usr/bin/env python3

import fileinput
import hashlib
import os
import random
import shutil
import stat
import subprocess
import sys

from src import config
from src import util
from src.repository import Repository

# Locations relative to the source tree.
DIR_ROOT = os.getcwd()
DIR_DISTFILES = os.path.join(DIR_ROOT, '_obj/distfiles')
DIR_INSTALL = os.path.join(DIR_ROOT, '_obj/install')
DIR_PACKAGES = os.path.join(DIR_ROOT, '_obj/packages')
DIR_REPOSITORY = os.path.join(DIR_ROOT, 'packages')

# Parse all of the BUILD rules.
repo = Repository(DIR_INSTALL)
for filename in util.walk_files(DIR_REPOSITORY):
    if os.path.basename(filename) == 'BUILD':
        repo.add_build_file(filename, DIR_DISTFILES)
target_packages = repo.get_target_packages()


def build_packages(package):
    # Build a package for Debian.
    path = package.create_debian_package()
    target = os.path.join(DIR_PACKAGES, 'debian', os.path.basename(path))
    util.make_parent_dir(target)
    os.rename(path, target)

    # Build a package for FreeBSD.
    path = package.create_freebsd_package()
    target = os.path.join(DIR_PACKAGES, 'freebsd', os.path.basename(path))
    util.make_parent_dir(target)
    os.rename(path, target)

if len(sys.argv) > 1:
    # Only build the packages provided on the command line.
    for name in set(sys.argv[1:]):
        for arch in config.ARCHITECTURES:
            build_packages(target_packages[(name, arch)])
else:
    # Build all packages.
    for package in target_packages.values():
        build_packages(package)
