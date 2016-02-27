# Copyright (c) 2015 Nuxi, https://nuxi.nl/
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
    version='1.21',
    homepage='https://www.gnupg.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libgpg-error-1.21.tar.bz2',
    checksum='b7dbdb3cad63a740e9f0c632a1da32d4afdb694ec86c8625c98ea0691713b84d',
    master_sites={'https://www.gnupg.org/ftp/gcrypt/libgpg-error/'},
    unsafe_string_sources={
        'src/estream.c',
        'src/estream-printf.c',
    },
)
