# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    # Freetype uses CC_BUILD instead of CC_FOR_BUILD.
    build = ctx.extract().gnu_configure(['CC_BUILD=' + ctx.host().cc()])
    build.make()
    stage = build.make_install()
    stage.path('bin/freetype-config').unhardcode_paths()
    stage.install()


package(
    name='freetype',
    version='2.8.1',
    homepage='http://www.freetype.org/',
    lib_depends={'bzip2', 'c-runtime', 'libpng', 'zlib'},
    build_cmd=build)

distfile(
    name='freetype-2.8.1.tar.bz2',
    checksum='e5435f02e02d2b87bb8e4efdcaa14b1f78c9cf3ab1ed80f94b6382fb6acc7d78',
    master_sites=sites_sourceforge('freetype/freetype2/2.8.1'),
    unsafe_string_sources={'include/freetype/config/ftstdlib.h'})
