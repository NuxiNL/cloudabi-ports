# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s_%(version)s')
    build = srcdir.path('source').cmake([
        '-DENABLE_CLI=OFF', '-DENABLE_SHARED=OFF',
    ])
    build.make()
    build.make_install().install()

package(
    name='x265',
    version='1.8',
    homepage='http://x265.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='x265_1.8.tar.gz',
    checksum='d41a3f0cc06dfc3967f6c47f458cb30b6aaa518f86c56c147946395bfe22b6f2',
    master_sites={'http://ftp.videolan.org/pub/videolan/x265/'},
    unsafe_string_sources={'source/common/common.h'},
)
