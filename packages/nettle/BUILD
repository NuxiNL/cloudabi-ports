# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-shared'])
    build.make(['SUBDIRS='])
    build.make_install(['SUBDIRS=', 'install']).install()


package(
    name='nettle',
    version='3.4',
    homepage='http://www.lysator.liu.se/~nisse/nettle/',
    lib_depends={'c-runtime', 'gmp'},
    build_cmd=build)

distfile(
    name='nettle-3.4.tar.gz',
    checksum='ae7a42df026550b85daca8389b6a60ba6313b0567f374392e54918588a411e94',
    master_sites=sites_gnu('nettle'))
