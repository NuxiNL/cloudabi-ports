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
    version='3.2.1',
    homepage='http://www.libarchive.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'xz'},
    build_cmd=build,
)

distfile(
    name='libarchive-3.2.1.tar.gz',
    checksum='72ee1a4e3fd534525f13a0ba1aa7b05b203d186e0c6072a8a4738649d0b3cfd2',
    master_sites={'http://www.libarchive.org/downloads/'},
)
