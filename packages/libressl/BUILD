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
    version='2.4.0',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.4.0.tar.gz',
    checksum='7e6000cfb9438fbfc7fe7fe0572af587e2f2a36bbdb95408e9874758d0c3382e',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
