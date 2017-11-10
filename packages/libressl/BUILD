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
    version='2.5.1',
    homepage='http://www.libressl.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libressl-2.5.1.tar.gz',
    checksum='f71ae0a824b78fb1a47ffa23c9c26e9d96c5c9b29234eacedce6b4c7740287cd',
    master_sites={'http://ftp.openbsd.org/pub/OpenBSD/LibreSSL/'})
