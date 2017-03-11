# Copyright (c) 2016-2017 Nuxi, https://nuxi.nl/
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
    version='1.3.2',
    homepage='https://xiph.org/flac/',
    lib_depends={'cxx-runtime', 'libogg'},
    build_cmd=build,
)

distfile(
    name='flac-1.3.2.tar.xz',
    checksum='91cfc3ed61dc40f47f050a109b08610667d73477af6ef36dcad31c31a4a8d53f',
    master_sites={'http://downloads.xiph.org/releases/flac/'},
    unsafe_string_sources={
        'src/libFLAC/metadata_iterators.c',
        'src/share/grabbag/cuesheet.c',
        'src/share/grabbag/replaygain.c',
        'src/share/utf8/iconvert.c',
        'src/share/utf8/utf8.c',
    },
)
