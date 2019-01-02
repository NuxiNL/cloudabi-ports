# Copyright (c) 2017-2019 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.cmake(['-DBUILD_TESTS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='flower',
    version='0.11',
    homepage='https://github.com/NuxiNL/flower',
    lib_depends={'arpc', 'cxx-runtime', 'jsoncpp'},
    build_cmd=build)

distfile(
    name='flower/v0.11.tar.gz',
    checksum='e213fa48f0abfa3095e07c3d8b95902511a42eb0cef902645418aef60cb32b3e',
    master_sites={'https://github.com/NuxiNL/flower/archive/'})
