# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.cmake(['-DBUILD_TESTS=OFF'])
    build.ninja()
    build.ninja_install().install()


package(
    name='arpc',
    version='0.4',
    homepage='https://github.com/NuxiNL/arpc',
    lib_depends={'cxx-runtime'},
    build_cmd=build)


def host_build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('scripts/aprotoc.py').install('bin/aprotoc')


host_package(
    name='arpc',
    version='0.4',
    homepage='https://github.com/NuxiNL/arpc',
    build_cmd=host_build)

distfile(
    name='arpc/v0.4.tar.gz',
    checksum='5f82d6deff33f332908105d3908a419d37df2bee1481511cde6e8d41e2ff2de9',
    master_sites={'https://github.com/NuxiNL/arpc/archive/'})
