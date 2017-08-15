# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)src2.src')
    c_sources = {
        'Unwind-sjlj.c',
        'UnwindLevel1-gcc-ext.c',
        'UnwindLevel1.c',
        'UnwindRegistersRestore.S',
        'UnwindRegistersSave.S',
    }
    cxx_sources = {'Unwind-EHABI.cpp', 'libunwind.cpp'}
    srcdir = root.path('src')
    libunwind = ctx.archive({
        srcdir.path(f).compile(['-I../include', '-fexceptions'])
        for f in c_sources
    } | {
        srcdir.path(f).compile(['-I../include', '-std=c++11'])
        for f in cxx_sources
    })

    libunwind.install('lib/libunwind.a')


package(
    name='libunwind',
    version='5.0.0',
    homepage='http://libcxx.llvm.org/',
    lib_depends={'c-runtime', 'libcxx'},
    build_cmd=build)

distfile(
    name='libunwind-5.0.0rc2.src.tar.xz',
    checksum='cfb739a323e45976cf60ef8d8e7d31ef1dc451482e6c87e0da77db6c112e7e8e',
    master_sites={'http://prereleases.llvm.org/5.0.0/rc2/'})
