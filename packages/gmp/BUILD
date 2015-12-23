# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf(['gmp_prog_cc_works=yes'])
    build.make()
    build.make_install().install()

package(
    name='gmp',
    version='6.1.0',
    homepage='https://gmplib.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='gmp-6.1.0.tar.xz',
    checksum='68dadacce515b0f8a54f510edf07c1b636492bcdb8e8d54c56eb216225d16989',
    master_sites={
        'https://gmplib.org/download/gmp/',
        'https://ftp.gnu.org/gnu/gmp/',
    },
    unsafe_string_sources={'printf/sprintffuns.c'},
)
