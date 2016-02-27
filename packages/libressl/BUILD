# Copyright (c) 2015 Nuxi, https://nuxi.nl/
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
    version='2.3.1',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.3.1.tar.gz',
    checksum='410b58db4ebbcab43c3357612e591094f64fb9339269caa2e68728e36f8d589e',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
