# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
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
    version='2.6.3',
    homepage='http://www.freetype.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'bzip2', 'c-runtime', 'libpng', 'zlib'},
    build_cmd=build,
)

distfile(
    name='freetype-2.6.3.tar.bz2',
    checksum='371e707aa522acf5b15ce93f11183c725b8ed1ee8546d7b3af549863045863a2',
    master_sites=sites_sourceforge('freetype/freetype2/2.6.3'),
    unsafe_string_sources={'include/freetype/config/ftstdlib.h'},
)
