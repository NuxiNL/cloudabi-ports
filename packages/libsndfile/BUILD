# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf([
        'ac_cv_c_byte_order=' + {
            'aarch64': 'little',
            'x86_64': 'little',
        }[ctx.cpu()],
    ])
    build.make(['bin_PROGRAMS=', 'man_MANS=', 'noinst_PROGRAMS='])
    build.make_install([
        'bin_PROGRAMS=', 'man_MANS=', 'noinst_PROGRAMS=', 'install',
    ]).install()

package(
    name='libsndfile',
    version='1.0.26',
    homepage='http://www.mega-nerd.com/libsndfile/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'flac', 'libogg', 'libvorbis', 'speex'},
    build_cmd=build,
)

distfile(
    name='libsndfile-1.0.26.tar.gz',
    checksum='cd6520ec763d1a45573885ecb1f8e4e42505ac12180268482a44b28484a25092',
    master_sites={'http://www.mega-nerd.com/libsndfile/files/'},
    unsafe_string_sources={'src/common.h'},
)
