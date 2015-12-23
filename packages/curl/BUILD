# Copyright (c) 2015 Nuxi, https://nuxi.nl/
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
    version='7.46.0',
    homepage='http://curl.haxx.se/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libressl', 'zlib'},
    build_cmd=build,
)

distfile(
    name='curl-7.46.0.tar.lzma',
    checksum='fe854a0dedf0a89da72aa1725d8ff66285b613d366a88f14681dacd824024087',
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
