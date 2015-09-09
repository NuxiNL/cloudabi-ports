class Version:
    def __init__(self, version):
        # Strip off trailing letter.
        if version[-1].isalpha():
            self._letter = version[-1]
            digits = version[:-1]
        else:
            self._letter = ''
            digits = version

        # Turn the numbers into a list of integer values.
        self._parts = [int(part) for part in digits.split('.')]

        # String representation should not be altered.
        if version != str(self):
            raise Exception('Version %s is not canonical', version)

    def __str__(self):
        return '.'.join(str(part) for part in self._parts) + self._letter
