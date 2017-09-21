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
    version='1.6.32',
    homepage='http://www.libpng.org/',
    lib_depends={'c-runtime', 'zlib'},
    build_cmd=build)

distfile(
    name='libpng-1.6.32.tar.xz',
    checksum='c918c3113de74a692f0a1526ce881dc26067763eb3915c57ef3a0f7b6886f59b',
    master_sites=sites_sourceforge('libpng/libpng16/1.6.32'))
