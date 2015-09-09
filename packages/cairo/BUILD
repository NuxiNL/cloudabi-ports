# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf([
        'ax_cv_c_float_words_bigendian=' + {'x86_64': 'no'}[ctx.cpu()],
        '--enable-xlib=no',
    ])
    build.make(['noinst_LTLIBRARIES=', 'noinst_PROGRAMS='])
    build.make_install([
        'noinst_LTLIBRARIES=', 'noinst_PROGRAMS=', 'install'
    ]).install()

package(
    name='cairo',
    version='1.14.2',
    homepage='http://cairographics.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libpng', 'pixman'},
    build_cmd=build,
)

distfile(
    name='cairo-1.14.2.tar.xz',
    checksum='c919d999ddb1bbbecd4bbe65299ca2abd2079c7e13d224577895afa7005ecceb',
    master_sites={'http://cairographics.org/releases/'},
    patches={
        'no-fopen',
        'no-printf',
        'no-strcpy',
    },
)
