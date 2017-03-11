# Copyright (c) 2016-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.make([
        'SHARED_LIBS=', 'SHARED_PROGRAMS=', 'STATIC_PROGRAMS=',
        'TARGET_OS=CloudABI',
    ])
    srcdir.path('include/leveldb').install('include/leveldb')
    srcdir.path('helpers/memenv/memenv.h').install('include/memenv/memenv.h')
    srcdir.path('out-static/libleveldb.a').install('lib/libleveldb.a')
    srcdir.path('out-static/libmemenv.a').install('lib/libmemenv.a')

package(
    name='leveldb',
    version='1.20',
    homepage='http://leveldb.org/',
    lib_depends={'cxx-runtime', 'snappy'},
    build_cmd=build,
)

distfile(
    name='leveldb/v1.20.tar.gz',
    checksum='f5abe8b5b209c2f36560b75f32ce61412f39a2922f7045ae764a2c23335b6664',
    master_sites={'https://github.com/google/leveldb/archive/'},
)
