# Copyright (c) 2017-2019 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.cmake(['-DBUILD_TESTS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='arpc',
    version='0.8',
    homepage='https://github.com/NuxiNL/arpc',
    lib_depends={'cxx-runtime'},
    build_cmd=build)


def host_build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('scripts/aprotoc.py').install('bin/aprotoc')


host_package(
    name='arpc',
    version='0.8',
    homepage='https://github.com/NuxiNL/arpc',
    build_cmd=host_build)

distfile(
    name='arpc/v0.8.tar.gz',
    checksum='338e897ee40d232e9e186a848c8fdc5c84bef2a63ec1319b60c63bf9b846397b',
    master_sites={'https://github.com/NuxiNL/arpc/archive/'})
