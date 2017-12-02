# Copyright (c) 2016-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract('%(name)s/%(version)s').cmake(
        ['-DSNAPPY_BUILD_TESTS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='snappy',
    version='1.1.7',
    homepage='https://google.github.io/snappy/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='snappy/1.1.7.tar.gz',
    checksum='3dfa02e873ff51a11ee02b9ca391807f0c8ea0529a4924afa645fbf97163f9d4',
    master_sites={'https://github.com/google/snappy/archive/'},
)
