# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf(['--disable-shared'])
    build.make(['SUBDIRS='])
    build.make_install(['SUBDIRS=', 'install']).install()

package(
    name='nettle',
    version='3.1.1',
    homepage='http://www.lysator.liu.se/~nisse/nettle/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'gmp'},
    build_cmd=build,
)

distfile(
    name='nettle-3.1.1.tar.gz',
    checksum='5fd4d25d64d8ddcb85d0d897572af73b05b4d163c6cc49438a5bfbb8ff293d4c',
    master_sites=sites_gnu('nettle'),
)
