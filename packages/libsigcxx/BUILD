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
    version='2.8.0',
    homepage='http://libsigc.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='libsigc++-2.8.0.tar.xz',
    checksum='774980d027c52947cb9ee4fac6ffe2ca60cc2f753068a89dfd281c83dbff9651',
    master_sites={'http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.8/'},
)
