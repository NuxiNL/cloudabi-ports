# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(inplace=True)
    build.make()
    build.make_install().install()


package(
    name='libmng',
    version='2.0.3',
    homepage='http://libmng.com/',
    lib_depends={'c-runtime', 'jpeg', 'lcms2', 'zlib'},
    build_cmd=build)

distfile(
    name='libmng-2.0.3.tar.xz',
    checksum='4a462fdd48d4bc82c1d7a21106c8a18b62f8cc0042454323058e6da0dbb57dd3',
    master_sites=sites_sourceforge('libmng/libmng-devel/2.0.3'))
