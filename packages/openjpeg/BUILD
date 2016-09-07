# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)s/v%(version)s').cmake([
        '-DBUILD_CODEC=NO', '-DBUILD_MJ2=NO',
    ])
    build.ninja()
    build.ninja_install().install()

package(
    name='openjpeg',
    version='2.1.1',
    homepage='http://www.openjpeg.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='openjpeg/v2.1.1.tar.gz',
    checksum='82c27f47fc7219e2ed5537ac69545bf15ed8c6ba8e6e1e529f89f7356506dbaa',
    master_sites={'https://github.com/uclouvain/openjpeg/archive/'},
    unsafe_string_sources={'src/lib/openjp2/j2k.c'},
)
