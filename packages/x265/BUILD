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
    version='1.9',
    homepage='http://x265.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='x265_1.9.tar.gz',
    checksum='3e4654133ed957a98708fdb4cb9a154d9e80922b84e26e43fc462a101c5b15c8',
    master_sites={'http://ftp.videolan.org/pub/videolan/x265/'},
    unsafe_string_sources={'source/common/common.h'},
)
