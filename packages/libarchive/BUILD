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
    version='3.2.0',
    homepage='http://www.libarchive.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'xz'},
    build_cmd=build,
)

distfile(
    name='libarchive-3.2.0.tar.gz',
    checksum='7bce45fd71ff01dc20d19edd78322d4965583d81b8bed8e26cacb65d6f5baa87',
    master_sites={'http://www.libarchive.org/downloads/'},
)
