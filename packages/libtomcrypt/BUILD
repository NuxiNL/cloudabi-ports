# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract('libtom/crypt-%(version)s')
    root.make([
        'CROSS_COMPILE=%s-' % ctx.gnu_triple(),
        'IGNORE_SPEED=yes',
    ])
    root.make_install([
        'INCPATH=%s/include' % ctx.prefix(),
        'LIBPATH=%s/lib' % ctx.prefix(),
        'NODOCS=yes',
        'install',
    ]).install()


package(
    name='libtomcrypt',
    version='1.18.0',
    homepage='http://www.libtom.net/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libtom/crypt-1.18.0.tar.xz',
    checksum='da9df56a314afaab71963aa71bb6a075ea6bdee3d4db4af045f6bfe23e88b87a',
    master_sites={
        'https://github.com/libtom/libtomcrypt/releases/download/v1.18.0/'
    },
    unsafe_string_sources={
        'src/misc/crypt/crypt_constants.c',
        'src/misc/crypt/crypt_sizes.c',
    })
