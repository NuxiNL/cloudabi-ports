# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract()
    root.run(['./configure', '--prefix=' + ctx.prefix(), '--static'])
    root.make(['libz.a'])
    root.make_install().install()


package(
    name='zlib',
    version='1.2.11',
    homepage='http://www.zlib.net/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='zlib-1.2.11.tar.xz',
    checksum='4ff941449631ace0d4d203e3483be9dbc9da454084111f97ea0a2114e19bf066',
    master_sites={'http://zlib.net/'})
