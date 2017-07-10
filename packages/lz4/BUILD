# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/r%(version)s').path('lib')
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
    version='131',
    homepage='https://lz4.github.io/lz4/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='lz4/r131.tar.gz',
    checksum='9d4d00614d6b9dec3114b33d1224b6262b99ace24434c53487a0c8fd0b18cfed',
    master_sites={'https://github.com/lz4/lz4/archive/'})
