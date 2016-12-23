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
        {srcdir.path(f).compile(['-I../include', '-fexceptions'])
         for f in c_sources} |
        {srcdir.path(f).compile(['-I../include', '-std=c++11'])
         for f in cxx_sources})

    libunwind.install('lib/libunwind.a')

package(
    name='libunwind',
    version='3.9.1',
    homepage='http://libcxx.llvm.org/',
    lib_depends={'c-runtime', 'libcxx'},
    build_cmd=build,
)

distfile(
    name='libunwind-3.9.1.src.tar.xz',
    checksum='0b0bc73264d7ab77d384f8a7498729e3c4da8ffee00e1c85ad02a2f85e91f0e6',
    master_sites={'http://llvm.org/releases/3.9.1/'},
)
