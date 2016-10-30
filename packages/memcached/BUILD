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
    version='1.4.32',
    homepage='https://memcached.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libevent'},
    build_cmd=build,
)

distfile(
    name='memcached-1.4.32.tar.gz',
    checksum='54bb9acd5fbbb73cd1fbfa67cbc6b301009a2835a26c8a4c3dba634a0c3d875d',
    master_sites={'https://memcached.org/files/'},
    unsafe_string_sources={'memcached.c'},
)
