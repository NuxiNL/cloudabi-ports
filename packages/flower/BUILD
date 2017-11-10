# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.cmake(['-DBUILD_TESTS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='flower',
    version='0.10',
    homepage='https://github.com/NuxiNL/flower',
    lib_depends={'arpc', 'cxx-runtime', 'jsoncpp'},
    build_cmd=build)

distfile(
    name='flower/v0.10.tar.gz',
    checksum='6af98bf7f598a41c40e4a9006b034943795f9bea453ea22b6c07aec57b851a30',
    master_sites={'https://github.com/NuxiNL/flower/archive/'})
