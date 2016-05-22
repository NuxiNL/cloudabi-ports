# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='snappy',
    version='1.1.3',
    homepage='https://google.github.io/snappy/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='snappy-1.1.3.tar.gz',
    checksum='2f1e82adf0868c9e26a5a7a3115111b6da7e432ddbac268a7ca2fae2a247eef3',
    master_sites={'https://github.com/google/snappy/releases/download/1.1.3/'},
)
