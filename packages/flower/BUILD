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
    version='0.1',
    homepage='https://github.com/NuxiNL/flower',
    lib_depends={'arpc', 'cxx-runtime'},
    build_cmd=build)

distfile(
    name='flower/v0.1.tar.gz',
    checksum='ffd0c6dc89e2df09fe513899801dfbc97c6711c3ee9f2cce48163733b60ea8dd',
    master_sites={'https://github.com/NuxiNL/flower/archive/'})
