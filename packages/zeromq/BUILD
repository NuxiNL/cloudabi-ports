# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
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
    version='4.2.2',
    homepage='http://zeromq.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='zeromq/v4.2.2.tar.gz',
    checksum='ea5eecbb9cc231a750535a7b74f887b18656014cc92601e8ab34734db799b796',
    master_sites={'https://github.com/zeromq/libzmq/archive/'},
    unsafe_string_sources={
        'src/ipc_listener.cpp',
        'src/udp_engine.cpp',
    })
