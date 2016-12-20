# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['--without-x'])
    build.make(['bin_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'man_MANS=', 'install']).install()

package(
    name='jasper',
    version='1.900.16',
    homepage='http://www.ece.uvic.ca/~frodo/jasper/',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='jasper-1.900.16.tar.gz',
    checksum='349f2261767c51a9e59e37025a027686f45f55cfbb8c46fd55c8697092f9f971',
    master_sites={'http://www.ece.uvic.ca/~frodo/jasper/software/'},
    unsafe_string_sources={
        'src/libjasper/base/jas_seq.c',
        'src/libjasper/base/jas_string.c',
        'src/libjasper/jp2/jp2_enc.c',
        'src/libjasper/jpc/jpc_enc.c',
        'src/libjasper/pnm/pnm_enc.c',
    },
)
