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
    version='2.4.1',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.4.1.tar.gz',
    checksum='121922b13169cd47a85e3e77f0bc129f8d04247193b42491cb1fab9074e80477',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
