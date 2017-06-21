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
    version='0.1',
    homepage='https://github.com/NuxiNL/arpc',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='arpc/v0.1.tar.gz',
    checksum='ba7bbf6ad14835a333f44726a37f545e30aba133c0a5f49c0e7ea2d44138edad',
    master_sites={'https://github.com/NuxiNL/arpc/archive/'},
)
