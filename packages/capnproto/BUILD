# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s').path('c++')
    build = srcdir.cmake(['-DBUILD_TESTING=OFF', '-DCAPNP_LITE=ON'])
    build.ninja()
    build.ninja_install().install()


package(
    name='capnproto',
    version='0.6.1',
    homepage='https://github.com/capnproto/capnproto',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='capnproto/v0.6.1.tar.gz',
    checksum='85210424c09693d8fe158c1970a2bca37af3a0424f02b263f566a1b8a5451a2d',
    master_sites={'https://github.com/capnproto/capnproto/archive/'},
    unsafe_string_sources={'c++/src/kj/string.c++'})
