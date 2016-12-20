# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('libsigc++-%(version)s').gnu_configure()
    build.make(['noinst_PROGRAMS='])
    stage = build.make_install(['noinst_PROGRAMS=', 'install'])
    stage.path(
        'share/devhelp/books/libsigc++-2.0/libsigc++-2.0.devhelp2'
    ).unhardcode_paths()
    stage.install()

package(
    name='libsigcxx',
    version='2.10.0',
    homepage='http://libsigc.sourceforge.net/',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='libsigc++-2.10.0.tar.xz',
    checksum='f843d6346260bfcb4426259e314512b99e296e8ca241d771d21ac64f28298d81',
    master_sites={'http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.10/'},
)
