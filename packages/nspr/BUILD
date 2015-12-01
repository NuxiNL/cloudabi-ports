# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    host_ctx = ctx.host()
    build = ctx.extract().autoconf([
        'HOST_CC=' + host_ctx.cc(),
        'HOST_CFLAGS=' + host_ctx.cflags(),
        'MDCPUCFG_H=_cloudabi.cfg',
    ])
    build.make()
    stage = build.make_install()
    stage.path('bin/nspr-config').unhardcode_paths()
    stage.install()

package(
    name='nspr',
    version='4.11',
    homepage='https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSPR',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='nspr-4.11.tar.gz',
    checksum='cb320a9eee7028275ac0fce7adc39dee36f14f02fd8432fce1b7e1aa5e3685c2',
    master_sites={'https://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v4.11/src/'},
    unsafe_string_sources={
        'lib/libc/src/strcat.c',
        'lib/libc/src/strcpy.c',
        'pr/src/io/prlayer.c',
        'pr/src/misc/pratom.c',
        'pr/src/misc/prcountr.c',
        'pr/src/misc/prerrortable.c',
        'pr/src/misc/prinit.c',
        'pr/src/misc/pripc.c',
        'pr/src/misc/prtrace.c',
        'pr/src/threads/prrwlock.c',
    },
)
