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
    version='3.5.0',
    homepage='https://developers.google.com/protocol-buffers/',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build)


def host_build(ctx):
    build = ctx.extract().path('cmake').cmake()
    build.ninja()
    build.ninja_install().install()


host_package(
    name='protobuf-cpp',
    version='3.5.0',
    homepage='https://developers.google.com/protocol-buffers/',
    build_depends={'cmake', 'ninja'},
    build_cmd=host_build)

distfile(
    name='protobuf-cpp-3.5.0.tar.gz',
    checksum='8dd6b051c2b39ab95dfe1f53cc5e1662ceb852d856db57d85751696859698551',
    master_sites={
        'https://github.com/google/protobuf/releases/download/v3.5.0/'
    },
    unsafe_string_sources={
        'src/google/protobuf/io/strtod.cc',
        'src/google/protobuf/stubs/strutil.cc',
    })
