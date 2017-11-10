#!/usr/bin/env python3
# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import logging
import os
import sys

from src import util
from src.repository import Repository

# Setup logging
logging.basicConfig(level=logging.INFO)

# Locations relative to the source tree.
DIR_ROOT = os.getcwd()
DIR_DISTFILES = os.path.join(DIR_ROOT, '_obj/distfiles')
DIR_TMP = os.path.join(DIR_ROOT, '_obj/fixup_patches')

# Parse all of the BUILD rules.
repo = Repository(None)
for filename in util.walk_files(sys.argv[1]):
    if os.path.basename(filename) == 'BUILD':
        repo.add_build_file(filename, DIR_DISTFILES)

# Regenerate all the patches.
for distfile in repo.get_distfiles():
    distfile.fixup_patches(DIR_TMP)
