# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--without-iconv'])
    build.make()
    build.make_install().install()


host_package(
    name='libarchive',
    version='3.3.1',
    homepage='http://www.libarchive.org/',
    lib_depends={'xz'},
    build_cmd=build)

distfile(
    name='libarchive-3.3.1.tar.gz',
    checksum='29ca5bd1624ca5a007aa57e16080262ab4379dbf8797f5c52f7ea74a3b0424e7',
    master_sites={'http://www.libarchive.org/downloads/'})
