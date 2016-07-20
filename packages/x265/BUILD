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
    version='2.0',
    homepage='http://x265.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='x265_2.0.tar.gz',
    checksum='5a7f6797bee33310c690be5d9a6c63125f36663ac3478e98ac6b6142a70bce1f',
    master_sites={'https://bitbucket.org/multicoreware/x265/downloads/'},
    unsafe_string_sources={'source/common/common.h'},
)
