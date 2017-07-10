# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()


package(
    name='lzo',
    version='2.10',
    homepage='http://www.oberhumer.com/opensource/lzo/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='lzo-2.10.tar.gz',
    checksum='c0f892943208266f9b6543b3ae308fab6284c5c90e627931446fb49b4221a072',
    master_sites={'http://www.oberhumer.com/opensource/lzo/download/'})
