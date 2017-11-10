# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.cmake(['-DBUILD_TESTS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='arpc',
    version='0.6',
    homepage='https://github.com/NuxiNL/arpc',
    lib_depends={'cxx-runtime'},
    build_cmd=build)


def host_build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('scripts/aprotoc.py').install('bin/aprotoc')


host_package(
    name='arpc',
    version='0.6',
    homepage='https://github.com/NuxiNL/arpc',
    build_cmd=host_build)

distfile(
    name='arpc/v0.6.tar.gz',
    checksum='22bb8bdadabb8793c01d3997e2992ea4e449b2bada62b93579f02358994838bd',
    master_sites={'https://github.com/NuxiNL/arpc/archive/'})
