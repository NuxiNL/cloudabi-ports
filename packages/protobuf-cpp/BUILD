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
    version='3.3.0',
    homepage='https://developers.google.com/protocol-buffers/',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build)


def host_build(ctx):
    build = ctx.extract().path('cmake').cmake()
    build.ninja()
    build.ninja_install().install()


host_package(
    name='protobuf-cpp',
    version='3.3.0',
    homepage='https://developers.google.com/protocol-buffers/',
    build_cmd=host_build)

distfile(
    name='protobuf-cpp-3.3.0.tar.gz',
    checksum='5e2587dea2f9287885e3b04d3a94ed4e8b9b2d2c5dd1f0032ceef3ea1d153bd7',
    master_sites={
        'https://github.com/google/protobuf/releases/download/v3.3.0/'
    },
    unsafe_string_sources={
        'src/google/protobuf/io/strtod.cc',
        'src/google/protobuf/stubs/strutil.cc',
    })
