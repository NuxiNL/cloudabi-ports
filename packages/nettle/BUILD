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
    version='3.3',
    homepage='http://www.lysator.liu.se/~nisse/nettle/',
    lib_depends={'c-runtime', 'gmp'},
    build_cmd=build)

distfile(
    name='nettle-3.3.tar.gz',
    checksum='46942627d5d0ca11720fec18d81fc38f7ef837ea4197c1f630e71ce0d470b11e',
    master_sites=sites_gnu('nettle'))
