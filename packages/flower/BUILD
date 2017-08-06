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
    name='flower',
    version='0.6',
    homepage='https://github.com/NuxiNL/flower',
    lib_depends={'arpc', 'cxx-runtime', 'jsoncpp'},
    build_cmd=build)

distfile(
    name='flower/v0.6.tar.gz',
    checksum='31b005919448939ff764ce1254ab9e34e4cabb116ca0283d03b364c26fbe8d49',
    master_sites={'https://github.com/NuxiNL/flower/archive/'})
