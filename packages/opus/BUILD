# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-extra-programs'])
    build.make()
    build.make_install().install()


package(
    name='opus',
    version='1.2.1',
    homepage='http://www.opus-codec.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='opus-1.2.1.tar.gz',
    checksum='cfafd339ccd9c5ef8d6ab15d7e1a412c054bf4cb4ecbbbcc78c12ef2def70732',
    master_sites={'http://downloads.xiph.org/releases/opus/'})
