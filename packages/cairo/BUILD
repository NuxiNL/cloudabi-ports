# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf([
        'ax_cv_c_float_words_bigendian=' + {
            'aarch64': 'no',
            'x86_64': 'no',
        }[ctx.cpu()],
        'ac_cv_func_mmap=no',
        '--enable-xlib=no',
    ])
    build.make(['noinst_LTLIBRARIES=', 'noinst_PROGRAMS='])
    build.make_install([
        'noinst_LTLIBRARIES=', 'noinst_PROGRAMS=', 'install'
    ]).install()

package(
    name='cairo',
    version='1.14.4',
    homepage='http://cairographics.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'freetype', 'libpng', 'pixman'},
    build_cmd=build,
)

distfile(
    name='cairo-1.14.4.tar.xz',
    checksum='f6ec9c7c844db9ec011f0d66b57ef590c45adf55393d1fc249003512522ee716',
    master_sites={'http://cairographics.org/releases/'},
    unsafe_string_sources={
        'src/cairo-cff-subset.c',
        'src/cairo-pdf-surface.c',
    },
)
