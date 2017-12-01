# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().cmake(['-DJAS_ENABLE_PROGRAMS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='jasper',
    version='2.0.14',
    homepage='http://www.ece.uvic.ca/~frodo/jasper/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='jasper-2.0.14.tar.gz',
    checksum='2a1f61e55afe8b4ce8115e1508c5d7cb314d56dfcc2dd323f90c072f88ccf57b',
    master_sites={'http://www.ece.uvic.ca/~frodo/jasper/software/'},
    unsafe_string_sources={
        'src/libjasper/base/jas_seq.c',
        'src/libjasper/base/jas_string.c',
        'src/libjasper/jp2/jp2_enc.c',
        'src/libjasper/jpc/jpc_enc.c',
        'src/libjasper/pnm/pnm_enc.c',
    })
