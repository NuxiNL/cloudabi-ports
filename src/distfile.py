# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import logging
import os
import random
import shutil
import subprocess
import urllib

from . import config
from . import util

log = logging.getLogger(__name__)


class Distfile:
    def __init__(self, distdir, name, checksum, master_sites, patches,
                 unsafe_string_sources):
        for patch in patches:
            if not os.path.isfile(patch):
                raise Exception('Patch %s does not exist' % patch)

        self._distdir = distdir
        self._name = name
        self._checksum = checksum
        self._patches = patches
        self._unsafe_string_sources = unsafe_string_sources
        self._pathname = os.path.join(distdir, self._name)

        # Compute distfile URLs based on the provided list of sites.
        # Also add fallback URLs in case the master sites are down.
        self._urls = {
            site + os.path.basename(self._name)
            for site in master_sites
        } | {site + self._name
             for site in config.FALLBACK_MIRRORS}

    @staticmethod
    def _apply_patch(patch, target):
        # Automatically determine the patchlevel by taking a look at the
        # first filename in the patch.
        patchlevel = 0
        with open(patch, 'rb') as f:
            for l in f.readlines():
                if l.startswith(b'--- '):
                    filename = str(
                        l[4:-1].split(b'\t', 1)[0], encoding='ASCII')
                    while True:
                        if os.path.exists(os.path.join(target, filename)):
                            # Correct patchlevel determined.
                            break
                        # Increment patchlevel once more.
                        s = filename.split('/', 1)
                        if len(s) < 2:
                            # File does not seem to exist at all. Don't
                            # compute the patchlevel for this patch.
                            patchlevel = 0
                            break
                        filename = s[1]
                        patchlevel += 1
                    break

        # Apply the patch.
        with open(patch) as f:
            subprocess.check_call(
                ['patch', '-d', target,
                 '-tsp%d' % patchlevel], stdin=f)

        # Delete .orig files that patch leaves behind.
        for path in util.walk_files(target):
            if path.endswith('.orig'):
                os.unlink(path)

    def _extract_unpatched(self, target):
        # Fetch and extract tarball.
        self._fetch()
        tar = os.path.join(config.DIR_BUILDROOT, 'bin/bsdtar')
        if not os.path.exists(tar):
            tar = 'tar'
        util.make_dir(target)
        subprocess.check_call([tar, '-xC', target, '-f', self._pathname])

        # Remove leading directory names.
        while True:
            entries = os.listdir(target)
            if len(entries) != 1:
                return target
            subdir = os.path.join(target, entries[0])
            if not os.path.isdir(subdir):
                return target
            target = subdir

    def _fetch(self):
        for i in range(10):
            log.info('CHECKSUM %s', self._pathname)
            # Validate the existing file on disk.
            try:
                if util.sha256(self._pathname).hexdigest() == self._checksum:
                    return
            except FileNotFoundError as e:
                log.warning(e)

            url = random.sample(self._urls, 1)[0]
            log.info('FETCH %s', url)
            try:
                util.make_parent_dir(self._pathname)
                with util.unsafe_fetch(url) as fin, open(self._pathname,
                                                         'wb') as fout:
                    shutil.copyfileobj(fin, fout)
            except ConnectionResetError as e:
                log.warning(e)
            except urllib.error.URLError as e:
                log.warning(e)
        raise Exception('Failed to fetch %s' % self._name)

    def extract(self, target):
        target = self._extract_unpatched(target)
        # Apply patches.
        for patch in self._patches:
            self._apply_patch(patch, target)
        # Add markers to sources that depend on unsafe string sources.
        for filename in self._unsafe_string_sources:
            path = os.path.join(target, filename)
            with open(path, 'rb') as fin, open(path + '.new', 'wb') as fout:
                fout.write(
                    bytes(
                        '#define _CLOUDLIBC_UNSAFE_STRING_FUNCTIONS\n',
                        encoding='ASCII'))
                fout.write(fin.read())
                os.rename(path + '.new', path)
        return target

    def fixup_patches(self, tmpdir):
        if not self._patches:
            return
        # Extract one copy of the code to diff against.
        util.remove(tmpdir)
        orig_dir = self._extract_unpatched(os.path.join(tmpdir, 'orig'))
        for path in util.walk_files(orig_dir):
            if path.endswith('.orig'):
                os.unlink(path)

        for patch in sorted(self._patches):
            log.info('FIXUP %s', patch)
            # Apply individual patches to the code.
            patched_dir = os.path.join(tmpdir, 'patched')
            util.remove(patched_dir)
            patched_dir = self._extract_unpatched(patched_dir)
            self._apply_patch(patch, patched_dir)

            # Generate a new patch.
            util.diff(orig_dir, patched_dir, patch)
