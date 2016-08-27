# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-3.9.0rc3.src')
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
    version='3.8.93',
    homepage='http://libcxx.llvm.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libcxx'},
    build_cmd=build,
)

distfile(
    name='libunwind-3.9.0rc3.src.tar.xz',
    checksum='e3585fef020111955af6f11f8597e2541428317d5019771dfecf7253cb660dce',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc3/'},
)
