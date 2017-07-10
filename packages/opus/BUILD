# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-extra-programs'])
    build.make()
    build.make_install().install()


package(
    name='opus',
    version='1.1.4',
    homepage='http://www.opus-codec.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='opus-1.1.4.tar.gz',
    checksum='9122b6b380081dd2665189f97bfd777f04f92dc3ab6698eea1dbb27ad59d8692',
    master_sites={'http://downloads.xiph.org/releases/opus/'})
