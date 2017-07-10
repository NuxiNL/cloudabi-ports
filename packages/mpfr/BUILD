# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

package(
    name='mpfr',
    version='3.1.5',
    homepage='http://www.mpfr.org/',
    lib_depends={'c-runtime', 'gmp'},
    build_cmd=build_autoconf_automake)

distfile(
    name='mpfr-3.1.5.tar.xz',
    checksum='015fde82b3979fbe5f83501986d328331ba8ddf008c1ff3da3c238f49ca062bc',
    master_sites={'http://www.mpfr.org/mpfr-current/'},
    unsafe_string_sources={
        'src/get_str.c',
        'src/vasprintf.c',
    })
