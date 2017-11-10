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
    version='1.26.0',
    homepage='https://nghttp2.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='nghttp2-1.26.0.tar.xz',
    checksum='7ac7ef5c83449303bf38d16eb45caa9e1bd0bb3abb2afc0ab1e6b3aadbded6dd',
    master_sites={
        'https://github.com/nghttp2/nghttp2/releases/download/v1.26.0/',
    })
