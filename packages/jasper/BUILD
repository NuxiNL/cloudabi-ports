# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf(['--without-x'])
    build.make(['bin_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'man_MANS=', 'install']).install()

package(
    name='jasper',
    version='1.900.1',
    homepage='http://www.ece.uvic.ca/~frodo/jasper/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='jasper-1.900.1.zip',
    checksum='6b905a9c2aca2e275544212666eefc4eb44d95d0a57e4305457b407fe63f9494',
    master_sites={'http://www.ece.uvic.ca/~frodo/jasper/software/'},
    unsafe_string_sources={
        'src/libjasper/base/jas_seq.c',
        'src/libjasper/base/jas_string.c',
        'src/libjasper/jp2/jp2_enc.c',
        'src/libjasper/jpc/jpc_enc.c',
        'src/libjasper/pnm/pnm_enc.c',
    },
)
