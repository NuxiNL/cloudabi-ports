# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract()
    build = srcdir.cmake([
        '-DYAML_CPP_BUILD_TESTS=OFF',
        '-DYAML_CPP_BUILD_TOOLS=OFF',
    ])
    build.ninja()
    build.ninja_install().install()


package(
    name='yaml-cpp',
    version='0.6.0',
    homepage='https://github.com/jbeder/yaml-cpp',
    lib_depends={'boost', 'cxx-runtime'},
    build_cmd=build)

distfile(
    name='yaml-cpp-0.6.0.tar.gz',
    checksum='e643119f1d629a77605f02096cc3ac211922d48e3db12249b06a3db810dd8756',
    master_sites={'https://github.com/jbeder/yaml-cpp/archive/'})
