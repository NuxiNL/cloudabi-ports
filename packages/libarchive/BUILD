# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['--without-iconv'])
    build.make()
    build.make_install().install()

host_package(
    name='libarchive',
    version='3.2.2',
    homepage='http://www.libarchive.org/',
    lib_depends={'xz'},
    build_cmd=build,
)

distfile(
    name='libarchive-3.2.2.tar.gz',
    checksum='691c194ee132d1f0f7a42541f091db811bc2e56f7107e9121be2bc8c04f1060f',
    master_sites={'http://www.libarchive.org/downloads/'},
)
