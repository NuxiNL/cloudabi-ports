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
    version='2.6',
    homepage='http://www.freetype.org/',
    maintainer='info@nuxi.nl',
    # TODO(ed): Depend on Harfbuzz.
    lib_depends={'bzip2', 'c-runtime', 'libpng', 'zlib'},
    build_cmd=build,
)

distfile(
    name='freetype-2.6.tar.bz2',
    checksum='8469fb8124764f85029cc8247c31e132a2c5e51084ddce2a44ea32ee4ae8347e',
    master_sites=sites_sourceforge('freetype/freetype2/2.6'),
)
