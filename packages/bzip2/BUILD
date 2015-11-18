# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    sources = {'blocksort.c', 'bzlib.c', 'compress.c', 'crctable.c',
               'decompress.c', 'huffman.c', 'randtable.c'}
    libbz2 = ctx.archive(root.path(f).compile() for f in sources)

    libbz2.install('lib/libbz2.a')
    root.path('bzlib.h').install('include/bzlib.h')

package(
    name='bzip2',
    version='1.0.6',
    homepage='http://www.bzip.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='bzip2-1.0.6.tar.gz',
    checksum='a2848f34fcd5d6cf47def00461fcb528a0484d8edef8208d6d2e2909dc61d9cd',
    master_sites={'http://www.bzip.org/1.0.6/'},
)
