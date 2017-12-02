# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s').path('lib')
    ctx.archive(
        srcdir.path(f).compile()
        for f in {
            'lz4.c',
            'lz4frame.c',
            'lz4hc.c',
            'xxhash.c',
        }).install('lib/liblz4.a')
    for i in {'lz4.h', 'lz4frame.h', 'lz4hc.h'}:
        srcdir.path(i).install('include/' + i)


package(
    name='lz4',
    version='1.8.0',
    homepage='https://lz4.github.io/lz4/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='lz4/v1.8.0.tar.gz',
    checksum='2ca482ea7a9bb103603108b5a7510b7592b90158c151ff50a28f1ca8389fccf6',
    master_sites={'https://github.com/lz4/lz4/archive/'})
