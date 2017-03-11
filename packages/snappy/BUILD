# Copyright (c) 2016-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='snappy',
    version='1.1.4',
    homepage='https://google.github.io/snappy/',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='snappy-1.1.4.tar.gz',
    checksum='134bfe122fd25599bb807bb8130e7ba6d9bdb851e0b16efcb83ac4f5d0b70057',
    master_sites={'https://github.com/google/snappy/releases/download/1.1.4/'},
)
