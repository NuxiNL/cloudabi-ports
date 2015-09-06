import hashlib
import os
import random
import subprocess
import urllib.request

from . import util


class Distfile:

    def __init__(self, distdir, patchdir, name, checksum, master_sites,
                 patches=frozenset()):
        self._distdir = distdir
        self._patchdir = patchdir

        self._name = name
        self._checksum = checksum
        self._master_sites = master_sites
        self._patches = patches

        self._pathname = os.path.join(distdir, self._name)

    def _fetch(self):
        for i in range(10):
            # Validate the existing file on disk.
            try:
                checksum = hashlib.sha256()
                with open(self._pathname, 'rb') as f:
                  while True:
                    data = f.read(16384)
                    if not data:
                      break
                    checksum.update(data)
                if checksum.hexdigest() == self._checksum:
                    return
            except FileNotFoundError:
                pass

            # Fetch file through HTTP/FTP.
            url = random.sample(self._master_sites, 1)[0] + self._name
            print('FETCH', url)
            with urllib.request.urlopen(url) as fin:
              util.make_parents(self._distdir)
              with open(self._pathname, 'wb') as fout:
                while True:
                  data = fin.read(16384)
                  if not data:
                    break
                  fout.write(data)
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
            with open(os.path.join(self._patchdir, patch)) as f:
                subprocess.check_call(['patch', '-d', target, '-tsp0'], stdin=f)

        # Delete .orig files that patch leaves behind.
        for dirname, filename in util.walk_files(target):
            if filename.endswith('.orig'):
                os.unlink(os.path.join(dirname, filename))
        return target
