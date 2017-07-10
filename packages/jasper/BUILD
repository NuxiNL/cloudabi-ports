# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().cmake()
    build.ninja()
    build.ninja_install().install()


package(
    name='jasper',
    version='2.0.12',
    homepage='http://www.ece.uvic.ca/~frodo/jasper/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='jasper-2.0.12.tar.gz',
    checksum='5b24faf5ed38670d6286e45ab7516b26458d05e7929b435afe569176765f4dda',
    master_sites={'http://www.ece.uvic.ca/~frodo/jasper/software/'},
    unsafe_string_sources={
        'src/libjasper/base/jas_seq.c',
        'src/libjasper/base/jas_string.c',
        'src/libjasper/jp2/jp2_enc.c',
        'src/libjasper/jpc/jpc_enc.c',
        'src/libjasper/pnm/pnm_enc.c',
    })
