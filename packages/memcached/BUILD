# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(['ac_cv_c_endian=' + ctx.endian()])
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='memcached',
    version='1.4.31',
    homepage='https://memcached.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libevent'},
    build_cmd=build,
)

distfile(
    name='memcached-1.4.31.tar.gz',
    checksum='77ce5f820bafe94c33bf7bd86268d9bcdb3b76f68128d795b106db53d528707f',
    master_sites={'https://memcached.org/files/'},
    unsafe_string_sources={'memcached.c'},
)
