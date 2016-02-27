# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-shared'])
    build.make(['SUBDIRS='])
    build.make_install(['SUBDIRS=', 'install']).install()

package(
    name='nettle',
    version='3.2',
    homepage='http://www.lysator.liu.se/~nisse/nettle/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'gmp'},
    build_cmd=build,
)

distfile(
    name='nettle-3.2.tar.gz',
    checksum='ea4283def236413edab5a4cf9cf32adf540c8df1b9b67641cfc2302fca849d97',
    master_sites=sites_gnu('nettle'),
)
