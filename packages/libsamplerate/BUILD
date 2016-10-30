# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    build = root.gnu_configure()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install(
        ['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install']).install()

package(
    name='libsamplerate',
    version='0.1.9',
    homepage='http://www.mega-nerd.com/SRC/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libsamplerate-0.1.9.tar.gz',
    checksum='0a7eb168e2f21353fb6d84da152e4512126f7dc48ccb0be80578c565413444c1',
    master_sites={'http://www.mega-nerd.com/SRC/'},
)
