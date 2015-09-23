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
    version='2.2.3',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.2.3.tar.gz',
    checksum='a1ccc21adf91d60e99246031b99c930c9af5e1b1b5a61b1bec87beef6f16d882',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
