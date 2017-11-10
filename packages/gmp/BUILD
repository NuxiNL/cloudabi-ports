# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['gmp_prog_cc_works=yes'])
    build.make()
    build.make_install().install()


package(
    name='gmp',
    version='6.1.2',
    homepage='https://gmplib.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='gmp-6.1.2.tar.xz',
    checksum='87b565e89a9a684fe4ebeeddb8399dce2599f9c9049854ca8c0dfbdea0e21912',
    master_sites=sites_gnu('gmp'),
    unsafe_string_sources={'printf/sprintffuns.c'})
