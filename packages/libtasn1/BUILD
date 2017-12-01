# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-gcc-warnings'])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    stage = build.make_install(
        ['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install'])
    stage.path('share/man/man1').remove()
    stage.install()


package(
    name='libtasn1',
    version='4.12',
    homepage='https://www.gnu.org/software/libtasn1/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libtasn1-4.12.tar.gz',
    checksum='6753da2e621257f33f5b051cc114d417e5206a0818fe0b1ecfd6153f70934753',
    master_sites=sites_gnu('libtasn1'),
    unsafe_string_sources={
        'lib/decoding.c',
        'lib/element.c',
        'lib/gstr.c',
        'lib/gstr.h',
        'lib/int.h',
        'lib/parser_aux.c',
    })
