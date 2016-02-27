# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make([
        'bin_PROGRAMS=', 'man_MANS=',
        'noinst_PROGRAMS=', 'noinst_LTLIBRARIES=',
    ])
    build.make_install([
        'bin_PROGRAMS=', 'man_MANS=',
        'noinst_PROGRAMS=', 'noinst_LTLIBRARIES=', 'install',
    ]).install()

package(
    name='flac',
    version='1.3.1',
    homepage='https://xiph.org/flac/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime', 'libogg'},
    build_cmd=build,
)

distfile(
    name='flac-1.3.1.tar.xz',
    checksum='4773c0099dba767d963fd92143263be338c48702172e8754b9bc5103efe1c56c',
    master_sites={'http://downloads.xiph.org/releases/flac/'},
    unsafe_string_sources={
        'src/libFLAC/metadata_iterators.c',
        'src/share/grabbag/cuesheet.c',
        'src/share/grabbag/replaygain.c',
        'src/share/utf8/iconvert.c',
        'src/share/utf8/utf8.c',
    },
)
