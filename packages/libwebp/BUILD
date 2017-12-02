# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

package(
    name='libwebp',
    version='0.6.1',
    homepage='https://developers.google.com/speed/webp/',
    lib_depends={'c-runtime'},
    build_cmd=build_autoconf_automake)

distfile(
    name='libwebp-0.6.1.tar.gz',
    checksum='06503c782d9f151baa325591c3579c68ed700ffc62d4f5a32feead0ff017d8ab',
    master_sites={'http://downloads.webmproject.org/releases/webp/'},
    unsafe_string_sources={'imageio/pnmdec.c'})
