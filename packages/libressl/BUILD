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
    version='2.5.0',
    homepage='http://www.libressl.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libressl-2.5.0.tar.gz',
    checksum='8652bf6b55ab51fb37b686a3f604a2643e0e8fde2c56e6a936027d12afda6eae',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'},
)
