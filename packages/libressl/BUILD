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
    version='2.4.2',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.4.2.tar.gz',
    checksum='5f87d778e5d62822d60e38fa9621c1c5648fc559d198ba314bd9d89cbf67d9e3',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
