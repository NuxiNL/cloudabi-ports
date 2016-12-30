# Copyright (c) 2016 Nuxi, https://nuxi.nl/
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
    version='1.19',
    homepage='http://leveldb.org/',
    lib_depends={'cxx-runtime', 'snappy'},
    build_cmd=build,
)

distfile(
    name='leveldb/v1.19.tar.gz',
    checksum='7d7a14ae825e66aabeb156c1c3fae9f9a76d640ef6b40ede74cc73da937e5202',
    master_sites={'https://github.com/google/leveldb/archive/'},
)
