# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

package(
    name='mpfr',
    version='3.1.6',
    homepage='http://www.mpfr.org/',
    lib_depends={'c-runtime', 'gmp'},
    build_cmd=build_autoconf_automake)

distfile(
    name='mpfr-3.1.6.tar.xz',
    checksum='7a62ac1a04408614fccdc506e4844b10cf0ad2c2b1677097f8f35d3a1344a950',
    master_sites={'http://www.mpfr.org/mpfr-current/'},
    unsafe_string_sources={
        'src/get_str.c',
        'src/vasprintf.c',
    })
