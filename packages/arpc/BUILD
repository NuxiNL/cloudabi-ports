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
    version='0.5',
    homepage='https://github.com/NuxiNL/arpc',
    lib_depends={'cxx-runtime'},
    build_cmd=build)


def host_build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('scripts/aprotoc.py').install('bin/aprotoc')


host_package(
    name='arpc',
    version='0.5',
    homepage='https://github.com/NuxiNL/arpc',
    build_cmd=host_build)

distfile(
    name='arpc/v0.5.tar.gz',
    checksum='754853d37d83138e62f23eff95be8b3fa200238387d83e83453e6a5519458bed',
    master_sites={'https://github.com/NuxiNL/arpc/archive/'})
