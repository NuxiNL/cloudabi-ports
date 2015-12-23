# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf(['--disable-extra-programs'])
    build.make()
    build.make_install().install()

package(
    name='opus',
    version='1.1.1',
    homepage='http://www.opus-codec.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='opus-1.1.1.tar.gz',
    checksum='9b84ff56bd7720d5554103c557664efac2b8b18acc4bbcc234cb881ab9a3371e',
    master_sites={'http://downloads.xiph.org/releases/opus/'},
)
