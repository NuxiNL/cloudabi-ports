# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.path('build/cmake').cmake([
        '-DZSTD_BUILD_PROGRAMS=OFF',
        '-DZSTD_BUILD_TESTS=OFF',
    ])
    build.ninja()
    stage = build.ninja_install()
    stage.path('include').install('include')
    stage.path('lib/libzstd.a').install('lib/libzstd.a')


package(
    name='zstd',
    version='1.3.2',
    homepage='https://facebook.github.io/zstd/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='zstd/v1.3.2.tar.gz',
    checksum='ac5054a3c64e6510bc1ae890d05e3d271cc33ceebc9d06ac9f08105766d2798a',
    master_sites={'https://github.com/facebook/zstd/archive/'})
