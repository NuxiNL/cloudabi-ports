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
    version='0.2',
    homepage='https://github.com/NuxiNL/arpc',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='arpc/v0.2.tar.gz',
    checksum='1dc3af67a287f0e773348dfb5abe2619159f91b8d27d4e8c66b81de04a25f3cb',
    master_sites={'https://github.com/NuxiNL/arpc/archive/'},
)
