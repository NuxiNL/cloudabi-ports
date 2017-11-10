# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

package(
    name='libvorbis',
    version='1.3.5',
    homepage='https://xiph.org/vorbis/',
    lib_depends={'c-runtime', 'libogg'},
    build_cmd=build_autoconf_automake)

distfile(
    name='libvorbis-1.3.5.tar.xz',
    checksum='54f94a9527ff0a88477be0a71c0bab09a4c3febe0ed878b24824906cd4b0e1d1',
    master_sites={'http://downloads.xiph.org/releases/vorbis/'},
    unsafe_string_sources={'lib/info.c'})
