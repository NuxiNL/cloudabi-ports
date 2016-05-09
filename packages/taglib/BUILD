# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().cmake()
    build.ninja()
    stage = build.ninja_install()
    stage.path('bin/taglib-config').unhardcode_paths()
    stage.install()

package(
    name='taglib',
    version='1.11',
    homepage='https://taglib.github.io/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='taglib-1.11.tar.gz',
    checksum='ed4cabb3d970ff9a30b2620071c2b054c4347f44fc63546dbe06f97980ece288',
    master_sites={'https://taglib.github.io/releases/'},
)
