# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
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
    version='1.6.28',
    homepage='http://www.libpng.org/',
    lib_depends={'c-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='libpng-1.6.28.tar.xz',
    checksum='d8d3ec9de6b5db740fefac702c37ffcf96ae46cb17c18c1544635a3852f78f7a',
    master_sites=sites_sourceforge('libpng/libpng16/1.6.28'),
)
