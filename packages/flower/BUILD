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
    version='0.2',
    homepage='https://github.com/NuxiNL/flower',
    lib_depends={'arpc', 'cxx-runtime'},
    build_cmd=build)

distfile(
    name='flower/v0.2.tar.gz',
    checksum='fb3ac09bb6c646ce6efdb50a091b6219941d5d559d2a3c4a21923dba4e1d2600',
    master_sites={'https://github.com/NuxiNL/flower/archive/'})
