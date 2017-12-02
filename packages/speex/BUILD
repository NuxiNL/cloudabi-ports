# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-binaries'])
    build.make()
    build.make_install().install()


package(
    name='speex',
    version='1.2.0',
    homepage='http://www.speex.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='speex-1.2.0.tar.gz',
    checksum='eaae8af0ac742dc7d542c9439ac72f1f385ce838392dc849cae4536af9210094',
    master_sites={'http://downloads.xiph.org/releases/speex/'})
