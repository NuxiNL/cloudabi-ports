# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

package(
    name='mpfr',
    version='3.1.3',
    homepage='http://www.mpfr.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'gmp'},
    build_cmd=build_autoconf_automake,
)

distfile(
    name='mpfr-3.1.3.tar.xz',
    checksum='6835a08bd992c8257641791e9a6a2b35b02336c8de26d0a8577953747e514a16',
    master_sites={'http://www.mpfr.org/mpfr-current/'},
    unsafe_string_sources={
        'src/get_str.c',
        'src/vasprintf.c',
    },
)
