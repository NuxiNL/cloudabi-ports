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
    version='0.4',
    homepage='https://github.com/NuxiNL/flower',
    lib_depends={'arpc', 'cxx-runtime', 'jsoncpp'},
    build_cmd=build)

distfile(
    name='flower/v0.4.tar.gz',
    checksum='4e19d02ff4099350cbf6778e9ce22b7145a1618a5a0c5261e2c00b1d6c7d22e3',
    master_sites={'https://github.com/NuxiNL/flower/archive/'})
