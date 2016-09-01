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
    version='1.4.27',
    homepage='https://memcached.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libevent'},
    build_cmd=build,
)

distfile(
    name='memcached-1.4.27.tar.gz',
    checksum='96a90e7abec041a3c03258b6ce01ab21be16a9c594b7891a55567428392e8fe7',
    master_sites={'https://memcached.org/files/'},
    unsafe_string_sources={'memcached.c'},
)
