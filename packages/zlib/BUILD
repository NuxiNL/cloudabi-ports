# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    root.run(['./configure', '--prefix=' + ctx.prefix(), '--static'])
    root.make(['libz.a'])
    root.make_install().install()

package(
    name='zlib',
    version='1.2.8',
    homepage='http://www.zlib.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='zlib-1.2.8.tar.xz',
    checksum='831df043236df8e9a7667b9e3bb37e1fcb1220a0f163b6de2626774b9590d057',
    master_sites={'http://zlib.net/'},
    patches={'no-gzopen'},
)
