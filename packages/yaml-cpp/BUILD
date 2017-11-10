# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract()
    build = srcdir.cmake(['-DYAML_CPP_BUILD_TOOLS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='yaml-cpp',
    version='0.5.3',
    homepage='https://github.com/jbeder/yaml-cpp',
    lib_depends={'boost', 'cxx-runtime'},
    build_cmd=build)

distfile(
    name='yaml-cpp-0.5.3.tar.gz',
    checksum='decc5beabb86e8ed9ebeb04358d5363a5c4f72d458b2c788cb2f3ac9c19467b2',
    master_sites={'https://github.com/jbeder/yaml-cpp/archive/'})
