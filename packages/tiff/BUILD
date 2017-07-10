# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'noinst_PROGRAMS=',
                        'install']).install()


package(
    name='tiff',
    version='4.0.6',
    homepage='http://www.remotesensing.org/libtiff/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='tiff-4.0.6.tar.gz',
    checksum='4d57a50907b510e3049a4bba0d7888930fdfc16ce49f1bf693e5b6247370d68c',
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
    })
