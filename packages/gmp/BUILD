# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)s-6.0.0a').autoconf(['gmp_prog_cc_works=yes'])
    build.make()
    build.make_install().install()

package(
    name='gmp',
    version='6.0.0.1',
    homepage='https://gmplib.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='gmp-6.0.0a.tar.xz',
    checksum='9156d32edac6955bc53b0218f5f3763facb890b73a835d5e1b901dcf8eb8b764',
    master_sites={
        'https://gmplib.org/download/gmp/',
        'https://ftp.gnu.org/gnu/gmp/',
    },
    unsafe_string_sources={'printf/sprintffuns.c'},
)
