# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['ac_cv_c_byte_order=' + ctx.endian()])
    build.make(['bin_PROGRAMS=', 'man_MANS=', 'noinst_PROGRAMS='])
    build.make_install([
        'bin_PROGRAMS=',
        'man_MANS=',
        'noinst_PROGRAMS=',
        'install',
    ]).install()


package(
    name='libsndfile',
    version='1.0.28',
    homepage='http://www.mega-nerd.com/libsndfile/',
    lib_depends={'c-runtime', 'flac', 'libogg', 'libvorbis', 'speex'},
    build_cmd=build)

distfile(
    name='libsndfile-1.0.28.tar.gz',
    checksum='1ff33929f042fa333aed1e8923aa628c3ee9e1eb85512686c55092d1e5a9dfa9',
    master_sites={'http://www.mega-nerd.com/libsndfile/files/'},
    unsafe_string_sources={'src/common.h'})
