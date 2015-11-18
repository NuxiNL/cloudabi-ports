# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('libsigc++-%(version)s').autoconf()
    build.make(['noinst_PROGRAMS='])
    stage = build.make_install(['noinst_PROGRAMS=', 'install'])
    stage.path(
        'share/devhelp/books/libsigc++-2.0/libsigc++-2.0.devhelp2'
    ).unhardcode_paths()
    stage.install()

package(
    name='libsigcxx',
    version='2.6.2',
    homepage='http://libsigc.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='libsigc++-2.6.2.tar.xz',
    checksum='fdace7134c31de792c17570f9049ca0657909b28c4c70ec4882f91a03de54437',
    master_sites={'http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.6/'},
)
