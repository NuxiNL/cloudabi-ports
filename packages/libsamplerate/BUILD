# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    build = root.autoconf()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install(
        ['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install']).install()

package(
    name='libsamplerate',
    version='0.1.8',
    homepage='http://www.mega-nerd.com/SRC/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libsamplerate-0.1.8.tar.gz',
    checksum='93b54bdf46d5e6d2354b7034395fe329c222a966790de34520702bb9642f1c06',
    master_sites={'http://www.mega-nerd.com/SRC/'},
)
