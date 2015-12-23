# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # Freetype uses CC_BUILD instead of CC_FOR_BUILD.
    build = ctx.extract().autoconf(['CC_BUILD=' + ctx.host().cc()])
    build.make()
    stage = build.make_install()
    stage.path('bin/freetype-config').unhardcode_paths()
    stage.install()

package(
    name='freetype',
    version='2.6.2',
    homepage='http://www.freetype.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'bzip2', 'c-runtime', 'libpng', 'zlib'},
    build_cmd=build,
)

distfile(
    name='freetype-2.6.2.tar.bz2',
    checksum='baf6bdef7cdcc12ac270583f76ef245efe936267dbecef835f02a3409fcbb892',
    master_sites=sites_sourceforge('freetype/freetype2/2.6.2'),
    unsafe_string_sources={'include/freetype/config/ftstdlib.h'},
)
