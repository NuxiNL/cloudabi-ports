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
    version='2.6.5',
    homepage='http://www.freetype.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'bzip2', 'c-runtime', 'libpng', 'zlib'},
    build_cmd=build,
)

distfile(
    name='freetype-2.6.5.tar.bz2',
    checksum='e20a6e1400798fd5e3d831dd821b61c35b1f9a6465d6b18a53a9df4cf441acf0',
    master_sites=sites_sourceforge('freetype/freetype2/2.6.5'),
    unsafe_string_sources={'include/freetype/config/ftstdlib.h'},
)
