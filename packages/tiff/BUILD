# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install(
        ['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install']).install()

package(
    name='tiff',
    version='4.0.5',
    homepage='http://www.remotesensing.org/libtiff/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='tiff-4.0.5.tar.gz',
    checksum='e25eaa83ed7fab43ddd278b9b14d91a406a4b674cedc776adb95535f897f309c',
    master_sites={
        'ftp://ftp.remotesensing.org/pub/libtiff/',
        'http://download.osgeo.org/libtiff/',
    },
    unsafe_string_sources={
        'libtiff/tif_codec.c',
        'libtiff/tif_getimage.c',
        'libtiff/tif_compress.c',
        'libtiff/tif_extension.c',
        'libtiff/tif_open.c',
    },
)
