# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    ctx.extract('libunwind-%(version)s.src').rename(root.path('libunwind'))
    sources = {
        'abort_message.cpp',
        'cxa_aux_runtime.cpp',
        'cxa_default_handlers.cpp',
        'cxa_demangle.cpp',
        'cxa_exception.cpp',
        'cxa_exception_storage.cpp',
        'cxa_guard.cpp',
        'cxa_handlers.cpp',
        'cxa_noexception.cpp',
        'cxa_personality.cpp',
        'cxa_thread_atexit.cpp',
        'cxa_unexpected.cpp',
        'cxa_vector.cpp',
        'cxa_virtual.cpp',
        'fallback_malloc.cpp',
        'private_typeinfo.cpp',
        'stdlib_exception.cpp',
        'stdlib_new_delete.cpp',
        'stdlib_stdexcept.cpp',
        'stdlib_typeinfo.cpp',
    }
    srcdir = root.path('src')
    libcxxabi = ctx.archive(
        srcdir.path(f).compile([
            '-I../include', '-I../libunwind/include', '-std=c++11'
        ]) for f in sources)

    libcxxabi.install('lib/libc++abi.a')
    for f in {'include/cxxabi.h', 'include/__cxxabi_config.h'}:
        root.path(f).install(f)


package(
    name='libcxxabi',
    version='5.0.0',
    homepage='http://libcxxabi.llvm.org/',
    lib_depends={'c-runtime', 'libcxx'},
    build_cmd=build)

distfile(
    name='libcxxabi-5.0.0.src.tar.xz',
    checksum='176918c7eb22245c3a5c56ef055e4d69f5345b4a98833e0e8cb1a19cab6b8911',
    master_sites={'http://releases.llvm.org/5.0.0/'})
