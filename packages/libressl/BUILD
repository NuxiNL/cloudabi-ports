# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make()
    stage = build.make_install()
    stage.path('share/man/man1').remove()
    stage.install()

package(
    name='libressl',
    version='2.3.0',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.3.0.tar.gz',
    checksum='0451498d999ccff475226f5cfae07a3754a7b28c507c6bda007e316fc90d92a0',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
