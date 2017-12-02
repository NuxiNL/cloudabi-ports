# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install([
        'bin_PROGRAMS=',
        'noinst_PROGRAMS=',
        'install',
    ]).install()


package(
    name='tiff',
    version='4.0.9',
    homepage='http://www.libtiff.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='tiff-4.0.9.tar.gz',
    checksum='6e7bdeec2c310734e734d19aae3a71ebe37a4d842e0e23dbb1b8921c0026cfcd',
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
