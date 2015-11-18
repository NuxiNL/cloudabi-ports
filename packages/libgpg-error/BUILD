# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'man_MANS='])
    stage = build.make_install([
        'bin_PROGRAMS=', 'noinst_PROGRAMS=', 'man_MANS=', 'install',
    ])
    stage.path('bin/gpg-error-config').unhardcode_paths()
    stage.install()

package(
    name='libgpg-error',
    version='1.20',
    homepage='https://www.gnupg.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libgpg-error-1.20.tar.bz2',
    checksum='3266895ce3419a7fb093e63e95e2ee3056c481a9bc0d6df694cfd26f74e72522',
    master_sites={'https://www.gnupg.org/ftp/gcrypt/libgpg-error/'},
    unsafe_string_sources={
        'src/estream.c',
        'src/estream-printf.c',
    },
)
