# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.

import os
import random
import shutil
import subprocess
import urllib

from . import config
from . import util


class Distfile:

    def __init__(self, distdir, name, checksum, master_sites, patches):
        for patch in patches:
            if not os.path.isfile(patch):
                raise Exception('Patch %s does not exist' % patch)

        self._distdir = distdir
        self._name = name
        self._checksum = checksum
        # TODO(ed): Should append the directory name to FALLBACK_MIRRORS.
        self._master_sites = master_sites | config.FALLBACK_MIRRORS
        self._patches = patches
        self._pathname = os.path.join(distdir, self._name)

    def _fetch(self):
        for i in range(10):
            print('CHECKSUM', self._pathname)
            # Validate the existing file on disk.
            try:
                if util.sha256(self._pathname) == self._checksum:
                    return
            except FileNotFoundError as e:
                print(e)

            url = (random.sample(self._master_sites, 1)[0] +
                   os.path.basename(self._name))
            print('FETCH', url)
            try:
                util.make_parent_dir(self._pathname)
                with util.unsafe_fetch(url) as fin, open(self._pathname, 'wb') as fout:
                    shutil.copyfileobj(fin, fout)
            except urllib.error.URLError as e:
                print(e)
        raise Exception('Failed to fetch %s' % self._name)

    def extract(self, target):
        # Fetch and extract tarball.
        self._fetch()
        subprocess.check_call(['tar', '-xC', target, '-f', self._pathname])

        # Remove leading directory names.
        while True:
            entries = os.listdir(target)
            if len(entries) != 1:
                break
            subdir = os.path.join(target, entries[0])
            if not os.path.isdir(subdir):
                break
            target = subdir

        # Apply patches.
        for patch in self._patches:
            with open(patch) as f:
                subprocess.check_call(
                    ['patch', '-d', target, '-tsp0'], stdin=f)

        # Delete .orig files that patch leaves behind.
        for path in util.walk_files(target):
            if path.endswith('.orig'):
                os.unlink(path)
        return target
