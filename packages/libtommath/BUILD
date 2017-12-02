# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract('libtom/ltm-%(version)s')
    root.make([
        'CROSS_COMPILE=%s-' % ctx.gnu_triple(),
        'IGNORE_SPEED=yes',
        'default',
    ])
    root.make_install([
        'INCPATH=%s/include' % ctx.prefix(),
        'LIBPATH=%s/lib' % ctx.prefix(),
        'install',
    ]).install()


package(
    name='libtommath',
    version='1.0.1',
    homepage='http://www.libtom.net/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libtom/ltm-1.0.1.tar.xz',
    checksum='47032fb39d698ce4cf9c9c462c198e6b08790ce8203ad1224086b9b978636c69',
    master_sites={
        'https://github.com/libtom/libtommath/releases/download/v1.0.1/'
    })
