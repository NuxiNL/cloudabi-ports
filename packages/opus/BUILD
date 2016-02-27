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
    version='1.1.2',
    homepage='http://www.opus-codec.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='opus-1.1.2.tar.gz',
    checksum='0e290078e31211baa7b5886bcc8ab6bc048b9fc83882532da4a1a45e58e907fd',
    master_sites={'http://downloads.xiph.org/releases/opus/'},
)
