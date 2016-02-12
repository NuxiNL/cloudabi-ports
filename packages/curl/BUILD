# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf([
        '--disable-file', '--disable-ftp', '--disable-ntlm-wb',
        '--disable-tftp', '--enable-ipv6',
    ])
    build.make(['bin_PROGRAMS='])
    stage = build.make_install(['bin_PROGRAMS=', 'install'])
    stage.path('bin/curl-config').unhardcode_paths()
    stage.install()

package(
    name='curl',
    version='7.47.1',
    homepage='http://curl.haxx.se/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libressl', 'zlib'},
    build_cmd=build,
)

distfile(
    name='curl-7.47.1.tar.lzma',
    checksum='c9b2fd75417ff0a1d0cd1bb284d1d8d7a08963f945860c987d59ae0eb412aa01',
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
        'lib/version.c',
        'lib/vtls/openssl.c',
    },
)
