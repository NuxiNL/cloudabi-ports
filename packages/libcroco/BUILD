# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf(['--disable-Bsymbolic'])
    build.make()
    stage = build.make_install(['bin_PROGRAMS=', 'install'])
    stage.path('bin/croco-0.6-config').unhardcode_paths()
    stage.install()

package(
    name='libcroco',
    version='0.6.11',
    homepage='https://github.com/GNOME/libcroco',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'glib', 'libxml2'},
    build_cmd=build,
)

distfile(
    name='libcroco-0.6.11.tar.xz',
    checksum='132b528a948586b0dfa05d7e9e059901bca5a3be675b6071a90a90b81ae5a056',
    master_sites={'http://ftp.gnome.org/pub/GNOME/sources/libcroco/0.6/'},
)
