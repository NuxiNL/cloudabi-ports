# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract()
    for i in {
            'ipc_connecter', 'socks_connecter', 'tcp_connecter', 'udp_address',
            'udp_engine'
    }:
        srcdir.path('src').path(i + '.cpp').remove()
        srcdir.path('src').path(i + '.hpp').remove()
    build = srcdir.cmake(['-DWITH_PERF_TOOL=OFF', '-DZMQ_BUILD_TESTS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='zeromq',
    version='4.2.1',
    homepage='http://zeromq.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='zeromq-4.2.1.tar.gz',
    checksum='27d1e82a099228ee85a7ddb2260f40830212402c605a4a10b5e5498a7e0e9d03',
    master_sites={
        'https://github.com/zeromq/libzmq/releases/download/v4.2.1/'
    },
    unsafe_string_sources={
        'src/ipc_listener.cpp',
        'src/udp_engine.cpp',
    })
