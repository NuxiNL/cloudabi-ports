# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
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
    version='2.3',
    homepage='http://x265.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='x265_2.3.tar.gz',
    checksum='47520ac3424790168ea5c2db4a3cf12ca4d55a1790720007916652f07af3e41f',
    master_sites={'https://bitbucket.org/multicoreware/x265/downloads/'},
    unsafe_string_sources={'source/common/common.h'},
)
