# Copyright (c) 2015 Nuxi, https://nuxi.nl/
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
    version='1.14.6',
    homepage='http://cairographics.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'freetype', 'libpng', 'pixman'},
    build_cmd=build,
)

distfile(
    name='cairo-1.14.6.tar.xz',
    checksum='613cb38447b76a93ff7235e17acd55a78b52ea84a9df128c3f2257f8eaa7b252',
    master_sites={'http://cairographics.org/releases/'},
    unsafe_string_sources={
        'src/cairo-cff-subset.c',
        'src/cairo-pdf-surface.c',
    },
)
