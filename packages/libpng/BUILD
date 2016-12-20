# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    build = root.gnu_configure()
    build.make(['bin_PROGRAMS=', 'check_PROGRAMS='])
    stage = build.make_install(['bin_PROGRAMS=', 'check_PROGRAMS=', 'install'])
    stage.path('bin/libpng16-config').unhardcode_paths()
    stage.install()

package(
    name='libpng',
    version='1.6.26',
    homepage='http://www.libpng.org/',
    lib_depends={'c-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='libpng-1.6.26.tar.xz',
    checksum='266743a326986c3dbcee9d89b640595f6b16a293fd02b37d8c91348d317b73f9',
    master_sites=sites_sourceforge('libpng/libpng16/1.6.26'),
)
