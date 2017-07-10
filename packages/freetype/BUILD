# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # Freetype uses CC_BUILD instead of CC_FOR_BUILD.
    build = ctx.extract().gnu_configure(['CC_BUILD=' + ctx.host().cc()])
    build.make()
    stage = build.make_install()
    stage.path('bin/freetype-config').unhardcode_paths()
    stage.install()


package(
    name='freetype',
    version='2.7.1',
    homepage='http://www.freetype.org/',
    lib_depends={'bzip2', 'c-runtime', 'libpng', 'zlib'},
    build_cmd=build)

distfile(
    name='freetype-2.7.1.tar.bz2',
    checksum='3a3bb2c4e15ffb433f2032f50a5b5a92558206822e22bfe8cbe339af4aa82f88',
    master_sites=sites_sourceforge('freetype/freetype2/2.7.1'),
    unsafe_string_sources={'include/freetype/config/ftstdlib.h'})
