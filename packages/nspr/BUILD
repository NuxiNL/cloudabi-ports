# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    host_ctx = ctx.host()
    build = ctx.extract().gnu_configure([
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
    version='4.12',
    homepage='https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSPR',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='nspr-4.12.tar.gz',
    checksum='e0b10a1e569153668ff8bdea6c7e491b389fab69c2f18285a1ebf7c2ea4269de',
    master_sites={'https://ftp.mozilla.org/pub/mozilla.org/nspr/releases/v4.12/src/'},
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
