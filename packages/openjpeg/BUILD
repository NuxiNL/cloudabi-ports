# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract('%(name)s/v%(version)s').cmake([
        '-DBUILD_CODEC=NO',
        '-DBUILD_MJ2=NO',
    ])
    build.ninja()
    build.ninja_install().install()


package(
    name='openjpeg',
    version='2.1.2',
    homepage='http://www.openjpeg.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='openjpeg/v2.1.2.tar.gz',
    checksum='4ce77b6ef538ef090d9bde1d5eeff8b3069ab56c4906f083475517c2c023dfa7',
    master_sites={'https://github.com/uclouvain/openjpeg/archive/'},
    unsafe_string_sources={'src/lib/openjp2/j2k.c'})
