# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-gcc-warnings'])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    stage = build.make_install(
        ['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install'])
    stage.path('share/man/man1').remove()
    stage.install()

package(
    name='libtasn1',
    version='4.9',
    homepage='https://www.gnu.org/software/libtasn1/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libtasn1-4.9.tar.gz',
    checksum='4f6f7a8fd691ac2b8307c8ca365bad711db607d4ad5966f6938a9d2ecd65c920',
    master_sites=sites_gnu('libtasn1'),
    unsafe_string_sources={
        'lib/decoding.c',
        'lib/element.c',
        'lib/gstr.c',
        'lib/gstr.h',
        'lib/int.h',
        'lib/parser_aux.c',
    },
)
