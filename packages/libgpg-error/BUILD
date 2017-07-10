# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'man_MANS='])
    stage = build.make_install([
        'bin_PROGRAMS=',
        'noinst_PROGRAMS=',
        'man_MANS=',
        'install',
    ])
    stage.path('bin/gpg-error-config').unhardcode_paths()
    stage.install()


package(
    name='libgpg-error',
    version='1.27',
    homepage='https://www.gnupg.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libgpg-error-1.27.tar.bz2',
    checksum='4f93aac6fecb7da2b92871bb9ee33032be6a87b174f54abf8ddf0911a22d29d2',
    master_sites={'https://www.gnupg.org/ftp/gcrypt/libgpg-error/'},
    unsafe_string_sources={
        'src/estream.c',
        'src/estream-printf.c',
    })
