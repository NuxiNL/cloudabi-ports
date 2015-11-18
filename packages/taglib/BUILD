# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().cmake(['-DENABLE_STATIC=ON'])
    build.make()
    stage = build.make_install()
    stage.path('bin/taglib-config').unhardcode_paths()
    stage.install()

package(
    name='taglib',
    version='1.10',
    homepage='https://taglib.github.io/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='taglib-1.10.tar.gz',
    checksum='24c32d50042cb0ddf162eb263f8ac75c5a158e12bf32ed534c1d5c71ee369baa',
    master_sites={'https://taglib.github.io/releases/'},
)
