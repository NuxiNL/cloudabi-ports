# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.path('build/cmake').cmake(['-DPREFIX=' + ctx.prefix()])
    build.ninja()
    stage = build.ninja_install()
    stage.path('include').install('include')
    stage.path('lib/libzstd.a').install('lib/libzstd.a')

package(
    name='zstd',
    version='1.1.4',
    homepage='https://facebook.github.io/zstd/',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='zstd/v1.1.4.tar.gz',
    checksum='6aae2b586e359344cb8ecfe6917a407dc7e01b5d7d7388559714de37900fb9fb',
    master_sites={'https://github.com/facebook/zstd/archive/'},
)
