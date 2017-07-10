# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure([
        'GPG_ERROR_CONFIG=%s/bin/gpg-error-config' % ctx.localbase(),
    ])
    build.make(['noinst_PROGRAMS='])
    stage = build.make_install(['noinst_PROGRAMS=', 'install'])
    stage.path('bin/ksba-config').unhardcode_paths()
    stage.install()


package(
    name='libksba',
    version='1.3.5',
    homepage='https://www.gnupg.org/',
    lib_depends={'c-runtime', 'libgpg-error'},
    build_cmd=build)

distfile(
    name='libksba-1.3.5.tar.bz2',
    checksum='41444fd7a6ff73a79ad9728f985e71c9ba8cd3e5e53358e70d5f066d35c1a340',
    master_sites={'https://gnupg.org/ftp/gcrypt/libksba/'},
    unsafe_string_sources={
        'src/asn1-func.c',
        'src/asn1-func2.c',
        'src/asn1-parse.c',
        'src/cert.c',
        'src/certreq.c',
        'src/cms.c',
        'src/crl.c',
        'src/der-encoder.c',
        'src/keyinfo.c',
        'src/name.c',
        'src/ocsp.c',
        'src/oid.c',
        'src/time.c',
        'src/util.c',
    })
