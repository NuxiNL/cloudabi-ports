# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make()
    stage = build.make_install()
    stage.path('share/man/man1').remove()
    stage.install()

package(
    name='libressl',
    version='2.3.3',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.3.3.tar.gz',
    checksum='76733166187cc8587e0ebe1e83965ef257262a1a676a36806edd3b6d51b50aa9',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
