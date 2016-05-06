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
    version='2.3.4',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.3.4.tar.gz',
    checksum='7a1135b2620f78928e89538c211a4df1d9415994001d1e7c9178c6b6d72de6a9',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
