# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


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
    build_cmd=build,
)

distfile(
    name='yaml-cpp-0.5.3.tar.gz',
    checksum='668d7df0a43daba06e5b36aaa460ac902713ca4feb6b2d2697661607a0bc66ee',
    master_sites={'https://github.com/jbeder/yaml-cpp/archive/'},
)
