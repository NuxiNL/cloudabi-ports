# Copyright (c) 2015-2018 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract('%(name)s/v%(version)s')
    root.run(['./build'])

    root.run(['DESTDIR=stage', 'PREFIX=/', './install'])
    root.path('stage').install()


package(
    name='cloudlibc',
    version='0.102',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build)

distfile(
    name='cloudlibc/v0.102.tar.gz',
    checksum='e43bf6c07f840d32263945878f456a626d591ad76a40fb432c90c60ae69aa7db',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'})
