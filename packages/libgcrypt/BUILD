# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure([
        'GPG_ERROR_CONFIG=%s/bin/gpg-error-config' % ctx.localbase(),
    ])
    build.make(['bin_PROGRAMS=', 'man_MANS=', 'noinst_PROGRAMS='])
    stage = build.make_install([
        'bin_PROGRAMS=', 'man_MANS=', 'noinst_PROGRAMS=', 'install',
    ])
    stage.path('bin/libgcrypt-config').unhardcode_paths()
    stage.install()

package(
    name='libgcrypt',
    version='1.7.1',
    homepage='https://www.gnupg.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libgpg-error'},
    build_cmd=build,
)

distfile(
    name='libgcrypt-1.7.1.tar.bz2',
    checksum='450d9cfcbf1611c64dbe3bd04b627b83379ef89f11406d94c8bba305e36d7a95',
    master_sites={'https://www.gnupg.org/ftp/gcrypt/libgcrypt/'},
    unsafe_string_sources={
        'cipher/ecc-curves.c',
        'src/global.c',
        'src/misc.c',
        'src/sexp.c',
    },
)
