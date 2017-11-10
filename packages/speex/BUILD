# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract('%(name)s-1.2rc2').gnu_configure(
        ['--disable-binaries'])
    build.make()
    build.make_install().install()


package(
    name='speex',
    version='1.1.92',
    homepage='http://www.speex.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='speex-1.2rc2.tar.gz',
    checksum='caa27c7247ff15c8521c2ae0ea21987c9e9710a8f2d3448e8b79da9806bce891',
    master_sites={'http://downloads.xiph.org/releases/speex/'})
