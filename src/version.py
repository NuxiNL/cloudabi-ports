# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


class SimpleVersion:

    def __init__(self, version):
        # Turn the numbers into a list of integer values.
        self._numbers = [int(part) for part in version.split('.')]

        # String representation should not be altered.
        if version != str(self):
            raise Exception('Version %s is not canonical', version)

    def __eq__(self, other):
        return self._numbers == other._numbers

    def __lt__(self, other):
        return self._numbers < other._numbers

    def __str__(self):
        return '.'.join(str(part) for part in self._numbers)


class FullVersion:

    def __init__(self, epoch=0, version=SimpleVersion('0'), revision=1):
        self._epoch = epoch
        self._version = version
        self._revision = revision

    def __lt__(self, other):
        return ((self._epoch, self._version, self._revision) <
                (other._epoch, other._version, other._revision))

    def __str__(self):
        return self.get_debian_version()

    def bump_epoch_revision(self, other):
        if self._epoch > other._epoch:
            # Epoch counter is already larger. Skip.
            return
        self._epoch = other._epoch
        if self._version < other._version:
            # Version is decreasing. Increase the Epoch and reset the
            # revision number.
            self._epoch += 1
            self._revision = 1
        elif (self._version == other._version and self._revision < other._revision):
            # Package of the same version already exists. Ensure that we
            # don't decrement the revision number.
            self._revision = other._revision

    def bump_revision(self):
        return FullVersion(self._epoch, self._version, self._revision + 1)

    def get_archlinux_version(self):
        version = '%s-%d' % (self._version, self._revision)
        if self._epoch:
            version = '%d:' % self._epoch + version
        return version

    def get_cygwin_version(self):
        # TODO: Cygwin does not seem to support epoch numbers
        assert self._epoch == 0
        return '%s-%d' % (self._version, self._revision)

    def get_debian_version(self):
        version = str(self._version)
        if self._epoch:
            version = '%d:' % self._epoch + version
        version += '-%d' % self._revision
        return version

    def get_freebsd_version(self):
        version = '%s_%d' % (self._version, self._revision)
        if self._epoch:
            version += ',%d' % self._epoch
        return version

    def get_netbsd_version(self):
        # TODO(ed): NetBSD does not seem to support the Epoch numbers?
        assert self._epoch == 0
        return '%snb%d' % (self._version, self._revision)

    def get_openbsd_version(self):
        version = '%sp%d' % (self._version, self._revision)
        if self._epoch:
            version += 'v%d' % self._epoch
        return version

    @staticmethod
    def parse_archlinux(string):
        epoch = 0
        revision = 0
        # Parse leading Epoch number.
        s = string.split(':', 1)
        if len(s) == 2:
            epoch = int(s[0])
            string = s[1]
        # Parse trailing revision number.
        s = string.rsplit('-', 1)
        if len(s) == 2:
            string = s[0]
            revision = int(s[1])
        return FullVersion(epoch, SimpleVersion(string), revision)

    @staticmethod
    def parse_cygwin(string):
        revision = 0
        # Parse trailing revision number.
        s = string.rsplit('-', 1)
        if len(s) == 2:
            string = s[0]
            revision = int(s[1])
        return FullVersion(epoch, SimpleVersion(string), revision)

    @staticmethod
    def parse_debian(string):
        epoch = 0
        revision = 0
        # Parse leading Epoch number.
        s = string.split(':', 1)
        if len(s) == 2:
            epoch = int(s[0])
            string = s[1]
        # Parse trailing revision number.
        s = string.rsplit('-', 1)
        if len(s) == 2:
            string = s[0]
            revision = int(s[1])
        return FullVersion(epoch, SimpleVersion(string), revision)

    @staticmethod
    def parse_freebsd(string):
        epoch = 0
        revision = 0
        # Parse trailing Epoch number.
        s = string.rsplit(',', 1)
        if len(s) == 2:
            string = s[0]
            epoch = int(s[1])
        # Parse trailing revision number.
        s = string.rsplit('_', 1)
        if len(s) == 2:
            string = s[0]
            revision = int(s[1])
        return FullVersion(epoch, SimpleVersion(string), revision)
