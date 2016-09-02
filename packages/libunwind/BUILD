# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    c_sources = {
        'Unwind-sjlj.c', 'UnwindLevel1-gcc-ext.c', 'UnwindLevel1.c',
        'UnwindRegistersRestore.S', 'UnwindRegistersSave.S',
    }
    cxx_sources = {'Unwind-EHABI.cpp', 'libunwind.cpp'}
    srcdir = root.path('src')
    libunwind = ctx.archive(
        {srcdir.path(f).compile(['-I../include'])
         for f in c_sources} |
        {srcdir.path(f).compile(['-I../include', '-std=c++11'])
         for f in cxx_sources})

    libunwind.install('lib/libunwind.a')

package(
    name='libunwind',
    version='3.9.0',
    homepage='http://libcxx.llvm.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libcxx'},
    build_cmd=build,
)

distfile(
    name='libunwind-3.9.0.src.tar.xz',
    checksum='66675ddec5ba0d36689757da6008cb2596ee1a9067f4f598d89ce5a3b43f4c2b',
    master_sites={'http://llvm.org/releases/3.9.0/'},
)
