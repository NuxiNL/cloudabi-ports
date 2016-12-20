# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-extra-programs'])
    build.make()
    build.make_install().install()

package(
    name='opus',
    version='1.1.3',
    homepage='http://www.opus-codec.org/',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='opus-1.1.3.tar.gz',
    checksum='58b6fe802e7e30182e95d0cde890c0ace40b6f125cffc50635f0ad2eef69b633',
    master_sites={'http://downloads.xiph.org/releases/opus/'},
)
