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
    version='2.7',
    homepage='http://www.freetype.org/',
    lib_depends={'bzip2', 'c-runtime', 'libpng', 'zlib'},
    build_cmd=build,
)

distfile(
    name='freetype-2.7.tar.bz2',
    checksum='d6a451f5b754857d2aa3964fd4473f8bc5c64e879b24516d780fb26bec7f7d48',
    master_sites=sites_sourceforge('freetype/freetype2/2.7'),
    unsafe_string_sources={'include/freetype/config/ftstdlib.h'},
)
