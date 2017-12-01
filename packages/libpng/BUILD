# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract()
    build = root.gnu_configure()
    build.make(['bin_PROGRAMS=', 'check_PROGRAMS='])
    stage = build.make_install(['bin_PROGRAMS=', 'check_PROGRAMS=', 'install'])
    stage.path('bin/libpng16-config').unhardcode_paths()
    stage.install()


package(
    name='libpng',
    version='1.6.34',
    homepage='http://www.libpng.org/',
    lib_depends={'c-runtime', 'zlib'},
    build_cmd=build)

distfile(
    name='libpng-1.6.34.tar.xz',
    checksum='2f1e960d92ce3b3abd03d06dfec9637dfbd22febf107a536b44f7a47c60659f6',
    master_sites=sites_sourceforge('libpng/libpng16/1.6.34'))
