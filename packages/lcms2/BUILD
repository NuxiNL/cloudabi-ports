# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['ac_cv_lib_tiff_TIFFOpen=yes'])
    build.make()
    build.make_install().install()


package(
    name='lcms2',
    version='2.9',
    homepage='http://www.littlecms.com/',
    lib_depends={'c-runtime', 'jpeg', 'tiff', 'zlib'},
    build_cmd=build)

distfile(
    name='lcms2-2.9.tar.gz',
    checksum='48c6fdf98396fa245ed86e622028caf49b96fa22f3e5734f853f806fbc8e7d20',
    master_sites=sites_sourceforge('lcms/lcms/2.9'),
    unsafe_string_sources={
        'src/cmscgats.c',
        'src/cmsnamed.c',
        'src/cmsps2.c',
    })
