# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['ac_cv_c_byte_order=' + ctx.endian()])
    build.make(['bin_PROGRAMS=', 'man_MANS=', 'noinst_PROGRAMS='])
    build.make_install([
        'bin_PROGRAMS=', 'man_MANS=', 'noinst_PROGRAMS=', 'install',
    ]).install()

package(
    name='libsndfile',
    version='1.0.27',
    homepage='http://www.mega-nerd.com/libsndfile/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'flac', 'libogg', 'libvorbis', 'speex'},
    build_cmd=build,
)

distfile(
    name='libsndfile-1.0.27.tar.gz',
    checksum='a391952f27f4a92ceb2b4c06493ac107896ed6c76be9a613a4731f076d30fac0',
    master_sites={'http://www.mega-nerd.com/libsndfile/files/'},
    unsafe_string_sources={'src/common.h'},
)
