# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


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
    version='3.4.1',
    homepage='https://developers.google.com/protocol-buffers/',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build)


def host_build(ctx):
    build = ctx.extract().path('cmake').cmake()
    build.ninja()
    build.ninja_install().install()


host_package(
    name='protobuf-cpp',
    version='3.4.1',
    homepage='https://developers.google.com/protocol-buffers/',
    build_depends={'cmake', 'ninja'},
    build_cmd=host_build)

distfile(
    name='protobuf-cpp-3.4.1.tar.gz',
    checksum='2bb34b4a8211a30d12ef29fd8660995023d119c99fbab2e5fe46f17528c9cc78',
    master_sites={
        'https://github.com/google/protobuf/releases/download/v3.4.1/'
    },
    unsafe_string_sources={
        'src/google/protobuf/io/strtod.cc',
        'src/google/protobuf/stubs/strutil.cc',
    })
