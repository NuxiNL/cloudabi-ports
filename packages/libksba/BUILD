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
    version='1.3.4',
    homepage='https://www.gnupg.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libgpg-error'},
    build_cmd=build,
)

distfile(
    name='libksba-1.3.4.tar.bz2',
    checksum='f6c2883cebec5608692d8730843d87f237c0964d923bbe7aa89c05f20558ad4f',
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
    },
)
