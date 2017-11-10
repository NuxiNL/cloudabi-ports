# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install([
        'bin_PROGRAMS=',
        'noinst_PROGRAMS=',
        'install',
    ]).install()


package(
    name='giflib',
    version='5.1.4',
    homepage='http://giflib.sourceforge.net/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='giflib-5.1.4.tar.bz2',
    checksum='df27ec3ff24671f80b29e6ab1c4971059c14ac3db95406884fc26574631ba8d5',
    master_sites=sites_sourceforge('giflib'),
    unsafe_string_sources={
        'lib/gif_font.c',
        'util/getarg.c',
    })
