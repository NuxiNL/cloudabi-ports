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
    version='2.3.0',
    homepage='http://www.openjpeg.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='openjpeg/v2.3.0.tar.gz',
    checksum='3dc787c1bb6023ba846c2a0d9b1f6e179f1cd255172bde9eb75b01f1e6c7d71a',
    master_sites={'https://github.com/uclouvain/openjpeg/archive/'},
    unsafe_string_sources={'src/lib/openjp2/j2k.c'})
