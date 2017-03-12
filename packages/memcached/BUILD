# Copyright (c) 2016-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['ac_cv_c_endian=' + ctx.endian()])
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='memcached',
    version='1.4.35',
    homepage='https://memcached.org/',
    lib_depends={'c-runtime', 'libevent'},
    build_cmd=build,
)

distfile(
    name='memcached-1.4.35.tar.gz',
    checksum='f4815ac95aa06c0f360052a0a12010533b2b78c3bfe475b171606c1b61469476',
    master_sites={'https://memcached.org/files/'},
    unsafe_string_sources={'memcached.c'},
)
