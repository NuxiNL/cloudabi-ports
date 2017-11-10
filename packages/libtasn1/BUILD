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
    version='4.10',
    homepage='https://www.gnu.org/software/libtasn1/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libtasn1-4.10.tar.gz',
    checksum='681a4d9a0d259f2125713f2e5766c5809f151b3a1392fd91390f780b4b8f5a02',
    master_sites=sites_gnu('libtasn1'),
    unsafe_string_sources={
        'lib/decoding.c',
        'lib/element.c',
        'lib/gstr.c',
        'lib/gstr.h',
        'lib/int.h',
        'lib/parser_aux.c',
    })
