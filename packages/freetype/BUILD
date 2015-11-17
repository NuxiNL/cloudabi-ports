# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make()
    stage = build.make_install()
    stage.path('bin/freetype-config').unhardcode_paths()
    stage.install()

package(
    name='freetype',
    version='2.6.1',
    homepage='http://www.freetype.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'bzip2', 'c-runtime', 'libpng', 'zlib'},
    build_cmd=build,
)

distfile(
    name='freetype-2.6.1.tar.bz2',
    checksum='2f6e9a7de3ae8e85bdd2fe237e27d868d3ba7a27495e65906455c27722dd1a17',
    master_sites=sites_sourceforge('freetype/freetype2/2.6.1'),
    unsafe_string_sources={'include/freetype/config/ftstdlib.h'},
)
