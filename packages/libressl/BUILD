# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make()
    stage = build.make_install()
    stage.path('share/man/man1').remove()
    stage.install()


package(
    name='libressl',
    version='2.6.3',
    homepage='https://www.libressl.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libressl-2.6.3.tar.gz',
    checksum='aead6598263171b96970da0d881e616d0813b69b35ebdc5991f87ff2ea7f5c98',
    master_sites={'https://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'})
