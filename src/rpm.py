# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import struct

from typing import Any, Dict, Iterator, Iterable, Union

IndexEntry = Union['Int16', 'Int32', 'String', 'Bin', 'StringArray',
                   'I18NString']


class Header:
    """Class for generating binary RPM headers."""

    def __init__(self, entries: Dict[int, IndexEntry]) -> None:
        self._entries = entries

    def __bytes__(self) -> bytes:
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
            indices += struct.pack('>iiii', tag, value.type(), len(values),
                                   value.count())
            # Append the entry's value.
            values += value.encode()

        # Return indices and values with a header record in front of it.
        return (b'\x8e\xad\xe8\x01\x00\x00\x00\x00' + struct.pack(
            '>ii',
            len(indices) // 16, len(values)) + indices + values)


class Int16:
    """List of 16 bit signed integers."""

    def __init__(self, values: Iterator[Any]) -> None:
        self._values = list(values)

    @staticmethod
    def alignment() -> int:
        return 2

    def count(self) -> int:
        return len(self._values)

    def encode(self) -> bytes:
        return b''.join(struct.pack('>h', value) for value in self._values)

    @staticmethod
    def type() -> int:
        return 3


class Int32:
    """List of 32 bit signed integers."""

    def __init__(self, values: Iterable[int]) -> None:
        self._values = list(values)

    @staticmethod
    def alignment() -> int:
        return 4

    def count(self) -> int:
        return len(self._values)

    def encode(self) -> bytes:
        return b''.join(struct.pack('>i', value) for value in self._values)

    @staticmethod
    def type() -> int:
        return 4


class String:
    """Single C string."""

    def __init__(self, value: str) -> None:
        self._value = value

    @staticmethod
    def alignment() -> int:
        return 1

    @staticmethod
    def count() -> int:
        return 1

    def encode(self) -> bytes:
        return bytes(self._value, encoding='ASCII') + b'\0'

    @staticmethod
    def type() -> int:
        return 6


class Bin:
    """Binary blob."""

    def __init__(self, value: bytes) -> None:
        self._value = value

    @staticmethod
    def alignment() -> int:
        return 1

    def count(self) -> int:
        return len(self._value)

    def encode(self) -> bytes:
        return self._value

    @staticmethod
    def type() -> int:
        return 7


class StringArray:
    """Sequence of C strings."""

    def __init__(self, values: Iterable[str]) -> None:
        self._values = list(values)

    @staticmethod
    def alignment() -> int:
        return 1

    def count(self) -> int:
        return len(self._values)

    def encode(self) -> bytes:
        return b''.join(
            bytes(value, encoding='ASCII') + b'\0' for value in self._values)

    @staticmethod
    def type() -> int:
        return 8


class I18NString:
    """Sequence of strings stored in a native character set.

    This implementation only supports ASCII."""

    def __init__(self, value: str) -> None:
        self._value = value

    @staticmethod
    def alignment() -> int:
        return 1

    @staticmethod
    def count() -> int:
        return 1

    def encode(self) -> bytes:
        return bytes(self._value, encoding='ASCII') + b'\0'

    @staticmethod
    def type() -> int:
        return 9
