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
    version='0.9',
    homepage='https://github.com/NuxiNL/flower',
    lib_depends={'arpc', 'cxx-runtime', 'jsoncpp'},
    build_cmd=build)

distfile(
    name='flower/v0.9.tar.gz',
    checksum='e712081eb5794245f4e27e591b1a1ea296c1bd6f2941afc2536c04be01355b10',
    master_sites={'https://github.com/NuxiNL/flower/archive/'})
