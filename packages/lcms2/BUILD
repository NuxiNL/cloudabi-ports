# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['ac_cv_lib_tiff_TIFFOpen=yes'])
    build.make()
    build.make_install().install()

package(
    name='lcms2',
    version='2.8',
    homepage='http://www.littlecms.com/',
    lib_depends={'c-runtime', 'jpeg', 'tiff', 'zlib'},
    build_cmd=build,
)

distfile(
    name='lcms2-2.8.tar.gz',
    checksum='66d02b229d2ea9474e62c2b6cd6720fde946155cd1d0d2bffdab829790a0fb22',
    master_sites=sites_sourceforge('lcms/lcms/2.8'),
    unsafe_string_sources={
        'src/cmscgats.c',
        'src/cmsnamed.c',
        'src/cmsps2.c',
    },
)
