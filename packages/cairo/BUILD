# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure([
        'ax_cv_c_float_words_bigendian=' + {
            'little': 'no',
            'big': 'yes',
        }[ctx.endian()],
        'ac_cv_func_mmap=no',
        '--enable-xlib=no',
    ])
    build.make(['noinst_LTLIBRARIES=', 'noinst_PROGRAMS='])
    build.make_install([
        'noinst_LTLIBRARIES=', 'noinst_PROGRAMS=', 'install'
    ]).install()

package(
    name='cairo',
    version='1.14.8',
    homepage='http://cairographics.org/',
    lib_depends={'c-runtime', 'freetype', 'libpng', 'pixman'},
    build_cmd=build,
)

distfile(
    name='cairo-1.14.8.tar.xz',
    checksum='d1f2d98ae9a4111564f6de4e013d639cf77155baf2556582295a0f00a9bc5e20',
    master_sites={
        'http://cairographics.org/releases/',
        'http://ftp.osuosl.org/pub/blfs/conglomeration/cairo/',
    },
    unsafe_string_sources={
        'src/cairo-cff-subset.c',
        'src/cairo-pdf-surface.c',
    },
)
