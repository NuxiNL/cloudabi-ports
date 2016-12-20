# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s_%(version)s')
    build = srcdir.path('source').cmake([
        '-DENABLE_CLI=OFF', '-DENABLE_SHARED=OFF',
    ])
    build.ninja()
    build.ninja_install().install()

package(
    name='x265',
    version='2.1',
    homepage='http://x265.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='x265_2.1.tar.gz',
    checksum='88fcb9af4ba52c0757ac9c0d8cd5ec79951a22905ae886897e06954353d6a643',
    master_sites={'https://bitbucket.org/multicoreware/x265/downloads/'},
    unsafe_string_sources={'source/common/common.h'},
)
