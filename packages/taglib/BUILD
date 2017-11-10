# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().cmake()
    build.ninja()
    stage = build.ninja_install()
    stage.path('bin/taglib-config').unhardcode_paths()
    stage.install()


package(
    name='taglib',
    version='1.11.1',
    homepage='https://taglib.github.io/',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build)

distfile(
    name='taglib-1.11.1.tar.gz',
    checksum='b6d1a5a610aae6ff39d93de5efd0fdc787aa9e9dc1e7026fa4c961b26563526b',
    master_sites={'https://taglib.github.io/releases/'})
