# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.cmake()
    build.ninja()
    build.ninja_install().install()


package(
    name='cloudabi-demo-webserver',
    version='0.2',
    homepage='https://github.com/NuxiNL/cloudabi-demo-webserver',
    lib_depends={'arpc', 'cxx-runtime', 'flower'},
    build_cmd=build)

distfile(
    name='cloudabi-demo-webserver/v0.2.tar.gz',
    checksum='fd9e4f0bb0e4f68e2ad7d85dbe48ef3b467037831b84cc8a071eff9f4eefb33e',
    master_sites={
        'https://github.com/NuxiNL/cloudabi-demo-webserver/archive/'
    })
