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
    version='1.6.23',
    homepage='http://www.libpng.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='libpng-1.6.23.tar.xz',
    checksum='6d921e7bdaec56e9f6594463ec1fe1981c3cd2d5fc925d3781e219b5349262f1',
    master_sites=sites_sourceforge('libpng/libpng16/1.6.23'),
)
