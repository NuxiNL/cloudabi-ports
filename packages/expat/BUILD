# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--without-xmlwf'])
    build.make()
    build.make_install().install()


package(
    name='expat',
    version='2.2.5',
    homepage='http://expat.sourceforge.net/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='expat-2.2.5.tar.bz2',
    checksum='d9dc32efba7e74f788fcc4f212a43216fc37cf5f23f4c2339664d473353aedf6',
    master_sites=sites_sourceforge('expat/expat/2.2.5'))
