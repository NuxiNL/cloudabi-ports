# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    build = root.autoconf()
    build.make(['bin_PROGRAMS=', 'check_PROGRAMS='])
    stage = build.make_install(['bin_PROGRAMS=', 'check_PROGRAMS=', 'install'])
    stage.path('bin/libpng16-config').unhardcode_paths()
    stage.install()

package(
    name='libpng',
    version='1.6.19',
    homepage='http://www.libpng.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='libpng-1.6.19.tar.xz',
    checksum='311c5657f53516986c67713c946f616483e3cdb52b8b2ee26711be74e8ac35e8',
    master_sites=sites_sourceforge('libpng/libpng16/1.6.19'),
)
