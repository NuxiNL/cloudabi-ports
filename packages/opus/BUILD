# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf(['--disable-extra-programs'])
    build.make()
    build.make_install().install()

package(
    name='opus',
    version='1.1',
    homepage='http://www.opus-codec.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='opus-1.1.tar.gz',
    checksum='b9727015a58affcf3db527322bf8c4d2fcf39f5f6b8f15dbceca20206cbe1d95',
    master_sites={'http://downloads.xiph.org/releases/opus/'},
)
