# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure([
        '--disable-file',
        '--disable-ftp',
        '--disable-ntlm-wb',
        '--disable-tftp',
        '--enable-ipv6',
    ])
    build.make(['bin_PROGRAMS='])
    stage = build.make_install(['bin_PROGRAMS=', 'install'])
    stage.path('bin/curl-config').unhardcode_paths()
    stage.install()


package(
    name='curl',
    version='7.50.3',
    homepage='http://curl.haxx.se/',
    lib_depends={'c-runtime', 'libressl', 'zlib'},
    build_cmd=build)

distfile(
    name='curl-7.50.3.tar.lzma',
    checksum='8c5457e2ecfc38d7e1103bf5e0f87895222340200de9ceefd300c3420698f5ea',
    master_sites={'http://curl.haxx.se/download/'},
    unsafe_string_sources={
        'lib/curl_sasl.c',
        'lib/ftp.c',
        'lib/imap.c',
        'lib/mprintf.c',
        'lib/progress.c',
        'lib/smb.c',
        'lib/socks.c',
        'lib/tftp.c',
        'lib/url.c',
        'lib/vauth/digest.c',
        'lib/version.c',
        'lib/vtls/openssl.c',
    })
