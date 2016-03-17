# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure([
        'ac_cv_c_endian=' + {
            'aarch64': 'little',
            'x86_64': 'little',
        }[ctx.cpu()],
    ])
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='memcached',
    version='1.4.25',
    homepage='https://memcached.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libevent'},
    build_cmd=build,
)

distfile(
    name='memcached-1.4.25.tar.gz',
    checksum='f058437b3c224d321919a9a6bb4e3eedb2312ed718c0caf087ff2f04ab795dda',
    master_sites={'https://memcached.org/files/'},
    unsafe_string_sources={'memcached.c'},
)
