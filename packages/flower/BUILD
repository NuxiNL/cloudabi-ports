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
    version='0.3',
    homepage='https://github.com/NuxiNL/flower',
    lib_depends={'arpc', 'cxx-runtime'},
    build_cmd=build)

distfile(
    name='flower/v0.3.tar.gz',
    checksum='67cfc43e36e5510649a65b85a226a2086c95288551b3ed91ac6ba2a29d7a5614',
    master_sites={'https://github.com/NuxiNL/flower/archive/'})
