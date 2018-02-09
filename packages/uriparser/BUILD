# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-doc', '--disable-test'])
    build.make(['bin_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'install']).install()


package(
    name='uriparser',
    version='0.8.5',
    homepage='https://uriparser.github.io/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='uriparser-0.8.5.tar.bz2',
    checksum='58eacd5c03d9e341c04eb0b30831faec89f3b415949ff8d72254e63432352cdd',
    master_sites={
        'https://github.com/uriparser/uriparser/releases/download/uriparser-0.8.5/'
    })
