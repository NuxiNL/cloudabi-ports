# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract('%(name)ssrc.v9b').gnu_configure()
    build.make(['bin_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'man_MANS=', 'install']).install()


package(
    name='jpeg',
    version='9.2',
    homepage='http://www.ijg.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='jpegsrc.v9b.tar.gz',
    checksum='240fd398da741669bf3c90366f58452ea59041cacc741a489b99f2f6a0bad052',
    master_sites={'http://www.ijg.org/files/'},
    unsafe_string_sources={'jerror.c'})
