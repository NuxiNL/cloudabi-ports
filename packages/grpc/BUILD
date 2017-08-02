# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('src/compiler').remove()
    host_prefix = ctx.host().prefix()
    build = srcdir.cmake([
        '-DgRPC_BUILD_TOOLS=OFF',
        '-DgRPC_BENCHMARK_PROVIDER=package',
        '-DgRPC_CARES_PROVIDER=package',
        '-DgRPC_GFLAGS_PROVIDER=package',
        '-DgRPC_PROTOBUF_PROVIDER=package',
        '-DgRPC_SSL_PROVIDER=package',
        '-DgRPC_ZLIB_PROVIDER=package',
        '-D_gRPC_PROTOBUF_PROTOC=%s/bin/protoc' % host_prefix,
        '-DgRPC_PROTOBUF_GRPC_CPP_PLUGIN=%s/bin/grpc_cpp_plugin' % host_prefix,
    ])
    build.ninja()
    build.ninja_install().install()


package(
    name='grpc',
    version='1.4.2',
    homepage='http://www.grpc.io/',
    lib_depends={'c-ares', 'cxx-runtime', 'libressl', 'protobuf-cpp'},
    build_cmd=build)


def host_build(ctx):
    build = ctx.extract('%(name)s/v%(version)s').cmake([
        '-DgRPC_CARES_PROVIDER=package',
        '-DgRPC_PROTOBUF_PROVIDER=package',
        '-DgRPC_SSL_PROVIDER=package',
        '-DgRPC_ZLIB_PROVIDER=package',
    ])
    build.ninja()
    build.ninja_install().install()


host_package(
    name='grpc',
    version='1.4.2',
    homepage='http://www.grpc.io/',
    build_depends={'c-ares', 'cmake', 'protobuf-cpp'},
    build_cmd=host_build)

distfile(
    name='grpc/v1.4.2.tar.gz',
    checksum='268481b9cd09aaa0758fcd14236537cbd3ebcd637f43150fdf7937582f2dc4dc',
    master_sites={'https://github.com/grpc/grpc/archive/'},
    unsafe_string_sources={
        'src/core/ext/filters/client_channel/resolver_registry.c',
        'src/core/ext/transport/cronet/client/secure/cronet_channel_create.c',
        'src/core/ext/transport/cronet/transport/cronet_transport.c',
        'src/core/lib/support/log_posix.c',
    })
