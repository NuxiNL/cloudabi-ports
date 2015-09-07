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
DIR_REPOSITORY = os.path.join(DIR_ROOT, 'packages')

# Parse all of the BUILD rules.
repo = Repository(DIR_INSTALL)
for dirname, filename in util.walk_files(DIR_REPOSITORY):
    if filename == 'BUILD':
        repo.add_build_file(os.path.join(dirname, 'BUILD'), DIR_DISTFILES)
target_packages = repo.get_target_packages()

if len(sys.argv) > 1:
    # Only build the packages provided on the command line.
    for name in set(sys.argv[1:]):
        for arch in config.ARCHITECTURES:
            target_packages[(name, arch)].build()
else:
    # Build all packages.
    for name, arch in target_packages:
        target_packages[(name, arch)].build()
