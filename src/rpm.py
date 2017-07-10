# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

import struct


class Header:
    """Class for generating binary RPM headers."""

    def __init__(self, entries):
        self._entries = entries

    def __bytes__(self):
        """Serializes a set of entries to a binary RPM header."""
        indices = b''
        values = b''
        for tag, value in sorted(self._entries.items()):
            if value.count() == 0:
                continue
            # Add padding that is necessary to get the alignment right.
            align = value.alignment()
            values += b'\0' * (((align - len(values)) % align) % align)
            # Create index entry.
            indices += struct.pack('>iiii', tag,
                                   value.type(), len(values), value.count())
            # Append the entry's value.
            values += value.encode()

        # Return indices and values with a header record in front of it.
        return (b'\x8e\xad\xe8\x01\x00\x00\x00\x00' + struct.pack(
            '>ii', len(indices) // 16, len(values)) + indices + values)


class Int16:
    """List of 16 bit signed integers."""

    def __init__(self, values):
        self._values = list(values)

    @staticmethod
    def alignment():
        return 2

    def count(self):
        return len(self._values)

    def encode(self):
        return b''.join(struct.pack('>h', value) for value in self._values)

    @staticmethod
    def type():
        return 3


class Int32:
    """List of 32 bit signed integers."""

    def __init__(self, values):
        self._values = list(values)

    @staticmethod
    def alignment():
        return 4

    def count(self):
        return len(self._values)

    def encode(self):
        return b''.join(struct.pack('>i', value) for value in self._values)

    @staticmethod
    def type():
        return 4


class String:
    """Single C string."""

    def __init__(self, value):
        self._value = value

    @staticmethod
    def alignment():
        return 1

    @staticmethod
    def count():
        return 1

    def encode(self):
        return bytes(self._value, encoding='ASCII') + b'\0'

    @staticmethod
    def type():
        return 6


class Bin:
    """Binary blob."""

    def __init__(self, value):
        self._value = value

    @staticmethod
    def alignment():
        return 1

    def count(self):
        return len(self._value)

    def encode(self):
        return self._value

    @staticmethod
    def type():
        return 7


class StringArray:
    """Sequence of C strings."""

    def __init__(self, values):
        self._values = list(values)

    @staticmethod
    def alignment():
        return 1

    def count(self):
        return len(self._values)

    def encode(self):
        return b''.join(
            bytes(value, encoding='ASCII') + b'\0' for value in self._values)

    @staticmethod
    def type():
        return 8


class I18NString:
    """Sequence of strings stored in a native character set.

    This implementation only supports ASCII."""

    def __init__(self, value):
        self._value = value

    @staticmethod
    def alignment():
        return 1

    @staticmethod
    def count():
        return 1

    def encode(self):
        return bytes(self._value, encoding='ASCII') + b'\0'

    @staticmethod
    def type():
        return 9
