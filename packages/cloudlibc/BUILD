# Copyright (c) 2015-2019 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract('%(name)s/v%(version)s')
    root.run(['./build'])

    root.run(['DESTDIR=stage', 'PREFIX=/', './install'])
    root.path('stage').install()


package(
    name='cloudlibc',
    version='0.103',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build)

distfile(
    name='cloudlibc/v0.103.tar.gz',
    checksum='952a20f5b01805095c0454bddba9a6cea60cc9dc7d8a7ba683373a6cc20d3776',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'})
