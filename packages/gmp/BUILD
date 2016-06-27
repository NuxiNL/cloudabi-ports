# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['gmp_prog_cc_works=yes'])
    build.make()
    build.make_install().install()

package(
    name='gmp',
    version='6.1.1',
    homepage='https://gmplib.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='gmp-6.1.1.tar.xz',
    checksum='d36e9c05df488ad630fff17edb50051d6432357f9ce04e34a09b3d818825e831',
    master_sites=sites_gnu('gmp'),
    unsafe_string_sources={'printf/sprintffuns.c'},
)
