class Version:
    def __init__(self, version):
        # Strip off trailing letter.
        if version[-1].isalpha():
            self._letter = version[-1]
            numbers = version[:-1]
        else:
            self._letter = ''
            numbers = version

        # Turn the numbers into a list of integer values.
        self._numbers = [int(part) for part in numbers.split('.')]

        # String representation should not be altered.
        if version != str(self):
            raise Exception('Version %s is not canonical', version)

    def __lt__(self, other):
        return (self._numbers, self._letter) < (other._numbers, other._letter)

    def __str__(self):
        return '.'.join(str(part) for part in self._numbers) + self._letter

class FullVersion:
    def __init__(self, epoch, version, revision):
        self._epoch = epoch
        self._version = version
        self._revision = revision

    def __str__(self):
        return self.get_freebsd_string()

    def get_debian(self):
        version = str(self._version)
        if self._epoch:
            version = '%d:' % self._epoch + version
        if self._revision:
            version += '_%d' % self._revision
        return version

    def get_freebsd(self):
        version = str(self._version)
        if self._revision:
            version += '_%d' % self._revision
        if self._epoch:
            version += ',%d' % self._epoch
        return version

    def bump_to_version(self, version):
        if version < self._version:
            # New version is lower. Increase the Epoch number.
            return FullVersion(self._epoch + 1, version, 0)
        elif self._version < version:
            # New version is higher. Reset the revision number.
            return FullVersion(self._epoch, version, 0)
        else:
            # Version is identical. Nothing to do.
            return self

    def bump_revision(self):
        return FullVersion(self._epoch, self._version, self._revision + 1)
