# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    srcdir.path('src/google/protobuf/compiler').remove()
    build = srcdir.path('cmake').cmake([
        '-Dprotobuf_BUILD_COMPILER=OFF',
        '-Dprotobuf_BUILD_TESTS=OFF',
        '-Dprotobuf_BUILD_EXAMPLES=OFF',
    ])
    build.ninja()
    build.ninja_install().install()


package(
    name='protobuf-cpp',
    version='3.4.0',
    homepage='https://developers.google.com/protocol-buffers/',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build)


def host_build(ctx):
    build = ctx.extract().path('cmake').cmake()
    build.ninja()
    build.ninja_install().install()


host_package(
    name='protobuf-cpp',
    version='3.4.0',
    homepage='https://developers.google.com/protocol-buffers/',
    build_cmd=host_build)

distfile(
    name='protobuf-cpp-3.4.0.tar.gz',
    checksum='71434f6f836a1e479c44008bb033b2a8b2560ff539374dcdefb126be739e1635',
    master_sites={
        'https://github.com/google/protobuf/releases/download/v3.4.0/'
    },
    unsafe_string_sources={
        'src/google/protobuf/io/strtod.cc',
        'src/google/protobuf/stubs/strutil.cc',
    })
