# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
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
    version='1.6.20',
    homepage='http://www.libpng.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='libpng-1.6.20.tar.xz',
    checksum='55c5959e9f3484d96141a3226c53bc9da42a4845e70879d3e1d6e94833d1918b',
    master_sites=sites_sourceforge('libpng/libpng16/1.6.20'),
)
