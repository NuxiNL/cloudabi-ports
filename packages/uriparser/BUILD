# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-doc', '--disable-test'])
    build.make(['bin_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'install']).install()


package(
    name='uriparser',
    version='0.8.4',
    homepage='http://uriparser.sourceforge.net/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='uriparser-0.8.4.tar.bz2',
    checksum='ce7ccda4136974889231e8426a785e7578e66a6283009cfd13f1b24a5e657b23',
    master_sites=sites_sourceforge('uriparser/Sources/0.8.4'))
