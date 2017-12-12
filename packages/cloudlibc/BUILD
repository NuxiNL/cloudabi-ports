# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract('%(name)s/v%(version)s')
    root.run(['./build'])

    root.run(['DESTDIR=stage', 'PREFIX=/', './install'])
    root.path('stage').install()


package(
    name='cloudlibc',
    version='0.96',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build)

distfile(
    name='cloudlibc/v0.96.tar.gz',
    checksum='07bd89ccc3a92f7653f54a5bc74fabf11e7657b422995e3a0b546e9b89824bef',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'})
