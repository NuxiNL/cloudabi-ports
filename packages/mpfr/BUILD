# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

package(
    name='mpfr',
    version='3.1.4',
    homepage='http://www.mpfr.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'gmp'},
    build_cmd=build_autoconf_automake,
)

distfile(
    name='mpfr-3.1.4.tar.xz',
    checksum='761413b16d749c53e2bfd2b1dfaa3b027b0e793e404b90b5fbaeef60af6517f5',
    master_sites={'http://www.mpfr.org/mpfr-current/'},
    unsafe_string_sources={
        'src/get_str.c',
        'src/vasprintf.c',
    },
)
