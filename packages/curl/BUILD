# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure([
        '--disable-file', '--disable-ftp', '--disable-ntlm-wb',
        '--disable-tftp', '--enable-ipv6',
    ])
    build.make(['bin_PROGRAMS='])
    stage = build.make_install(['bin_PROGRAMS=', 'install'])
    stage.path('bin/curl-config').unhardcode_paths()
    stage.install()

package(
    name='curl',
    version='7.49.1',
    homepage='http://curl.haxx.se/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libressl', 'zlib'},
    build_cmd=build,
)

distfile(
    name='curl-7.49.1.tar.lzma',
    checksum='540dd7e2017293ac13c925951a8e3187382b6fe7be045d5806912aae3c1f7c0c',
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
    },
)
