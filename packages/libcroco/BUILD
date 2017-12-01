# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--disable-Bsymbolic'])
    build.make()
    stage = build.make_install(['bin_PROGRAMS=', 'install'])
    stage.path('bin/croco-0.6-config').unhardcode_paths()
    stage.install()


package(
    name='libcroco',
    version='0.6.12',
    homepage='https://github.com/GNOME/libcroco',
    lib_depends={'c-runtime', 'glib', 'libxml2'},
    build_cmd=build)

distfile(
    name='libcroco-0.6.12.tar.xz',
    checksum='ddc4b5546c9fb4280a5017e2707fbd4839034ed1aba5b7d4372212f34f84f860',
    master_sites={'http://ftp.gnome.org/pub/GNOME/sources/libcroco/0.6/'})
