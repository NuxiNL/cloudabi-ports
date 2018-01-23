# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


class SimpleVersion:
    def __init__(self, version: str) -> None:
        # Turn the numbers into a list of integer values.
        self._numbers = [int(part) for part in version.split('.')]

        # String representation should not be altered.
        if version != str(self):
            raise Exception('Version %s is not canonical', version)

    def __eq__(self, other: object) -> bool:
        return isinstance(other,
                          SimpleVersion) and self._numbers == other._numbers

    def __lt__(self, other: 'SimpleVersion') -> bool:
        return self._numbers < other._numbers

    def __str__(self) -> str:
        return '.'.join(str(part) for part in self._numbers)


class FullVersion:
    def __init__(self,
                 epoch: int = 0,
                 version: SimpleVersion = SimpleVersion('0'),
                 revision: int = 1) -> None:
        self._epoch = epoch
        self._version = version
        self._revision = revision

    def __lt__(self, other: 'FullVersion') -> bool:
        return ((self._epoch, self._version, self._revision) <
                (other._epoch, other._version, other._revision))

    def __str__(self) -> str:
        return self.get_debian_version()

    def get_epoch(self) -> int:
        return self._epoch

    def get_version(self) -> SimpleVersion:
        return self._version

    def get_revision(self) -> int:
        return self._revision

    def bump_epoch_revision(self, other: 'FullVersion') -> None:
        if self._epoch > other._epoch:
            # Epoch counter is already larger. Skip.
            return
        self._epoch = other._epoch
        if self._version < other._version:
            # Version is decreasing. Increase the Epoch and reset the
            # revision number.
            self._epoch += 1
            self._revision = 1
        elif (self._version == other._version
              and self._revision < other._revision):
            # Package of the same version already exists. Ensure that we
            # don't decrement the revision number.
            self._revision = other._revision

    def bump_revision(self) -> 'FullVersion':
        return FullVersion(self._epoch, self._version, self._revision + 1)

    def get_archlinux_version(self) -> str:
        version = '%s-%d' % (self._version, self._revision)
        if self._epoch:
            version = '%d:' % self._epoch + version
        return version

    def get_cygwin_version(self) -> str:
        # TODO: Cygwin does not seem to support epoch numbers
        assert self._epoch == 0
        return '%s-%d' % (self._version, self._revision)

    def get_debian_version(self) -> str:
        version = str(self._version)
        if self._epoch:
            version = '%d:' % self._epoch + version
        version += '-%d' % self._revision
        return version

    def get_freebsd_version(self) -> str:
        version = '%s_%d' % (self._version, self._revision)
        if self._epoch:
            version += ',%d' % self._epoch
        return version

    def get_homebrew_version(self) -> str:
        # TODO(ed): Homebrew does not seem to support the Epoch numbers?
        assert self._epoch == 0
        return '%s_%d' % (self._version, self._revision)

    def get_netbsd_version(self) -> str:
        # TODO(ed): NetBSD does not seem to support the Epoch numbers?
        assert self._epoch == 0
        return '%snb%d' % (self._version, self._revision)

    def get_openbsd_version(self) -> str:
        version = '%sp%d' % (self._version, self._revision)
        if self._epoch:
            version += 'v%d' % self._epoch
        return version

    def get_redhat_version(self) -> str:
        version = '%s-%d' % (self._version, self._revision)
        if self._epoch:
            version = '%d:' % self._epoch + version
        return version

    @staticmethod
    def parse_archlinux(string: str) -> 'FullVersion':
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
    def parse_cygwin(string: str) -> 'FullVersion':
        revision = 0
        # Parse trailing revision number.
        s = string.rsplit('-', 1)
        if len(s) == 2:
            string = s[0]
            revision = int(s[1])
        return FullVersion(0, SimpleVersion(string), revision)

    @staticmethod
    def parse_debian(string: str) -> 'FullVersion':
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
    def parse_freebsd(string: str) -> 'FullVersion':
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

    @staticmethod
    def parse_homebrew(string: str) -> 'FullVersion':
        s = string.split('_', 1)
        return FullVersion(0, SimpleVersion(s[0]), int(s[1]))
