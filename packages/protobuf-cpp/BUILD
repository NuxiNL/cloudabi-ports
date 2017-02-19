# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    srcdir.path('src/google/protobuf/compiler').remove()
    build = srcdir.path('cmake').cmake([
        '-Dprotobuf_BUILD_TESTS=OFF',
        '-Dprotobuf_BUILD_EXAMPLES=OFF',
    ])
    build.ninja()
    build.ninja_install().install()

package(
    name='protobuf-cpp',
    version='3.2.0',
    homepage='https://developers.google.com/protocol-buffers/',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='protobuf-cpp-3.2.0.tar.gz',
    checksum='51d773e4297238b282eaa4c1dd317099675b12eef2b414732b851c00459225c6',
    master_sites={'https://github.com/google/protobuf/releases/download/v3.2.0/'},
    unsafe_string_sources={
        'src/google/protobuf/io/strtod.cc',
        'src/google/protobuf/stubs/strutil.cc',
    },
)
