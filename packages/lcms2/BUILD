# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['ac_cv_lib_tiff_TIFFOpen=yes'])
    build.make()
    build.make_install().install()

package(
    name='lcms2',
    version='2.7',
    homepage='http://www.littlecms.com/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'jpeg', 'tiff', 'zlib'},
    build_cmd=build,
)

distfile(
    name='lcms2-2.7.tar.gz',
    checksum='4524234ae7de185e6b6da5d31d6875085b2198bc63b1211f7dde6e2d197d6a53',
    master_sites=sites_sourceforge('lcms/lcms/2.7'),
    unsafe_string_sources={
        'src/cmscgats.c',
        'src/cmsnamed.c',
        'src/cmsps2.c',
    },
)
