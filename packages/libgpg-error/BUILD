# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'man_MANS='])
    stage = build.make_install([
        'bin_PROGRAMS=', 'noinst_PROGRAMS=', 'man_MANS=', 'install',
    ])
    stage.path('bin/gpg-error-config').unhardcode_paths()
    stage.install()

package(
    name='libgpg-error',
    version='1.23',
    homepage='https://www.gnupg.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libgpg-error-1.23.tar.bz2',
    checksum='7f0c7f65b98c4048f649bfeebfa4d4c1559707492962504592b985634c939eaa',
    master_sites={'https://www.gnupg.org/ftp/gcrypt/libgpg-error/'},
    unsafe_string_sources={
        'src/estream.c',
        'src/estream-printf.c',
    },
)
