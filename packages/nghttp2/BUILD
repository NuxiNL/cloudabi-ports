# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().cmake()
    build.ninja()
    stage = build.ninja_install()
    stage.path('share/man/man1').remove()
    stage.install()


package(
    name='nghttp2',
    version='1.28.0',
    homepage='https://nghttp2.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='nghttp2-1.28.0.tar.xz',
    checksum='0d6c3f00614deca3935e42a27f6ad0ea87c31d8c1baa3a9c52755955c599fd8d',
    master_sites={
        'https://github.com/nghttp2/nghttp2/releases/download/v1.28.0/',
    })
