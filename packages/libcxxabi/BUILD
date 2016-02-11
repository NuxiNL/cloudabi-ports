# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-3.8.0rc2.src')
    ctx.extract('libunwind-3.8.0rc2.src').rename(root.path('libunwind'))
    sources = {
        'abort_message.cpp', 'cxa_aux_runtime.cpp',
        'cxa_default_handlers.cpp', 'cxa_demangle.cpp',
        'cxa_exception.cpp', 'cxa_exception_storage.cpp', 'cxa_guard.cpp',
        'cxa_handlers.cpp', 'cxa_new_delete.cpp', 'cxa_personality.cpp',
        'cxa_thread_atexit.cpp', 'cxa_unexpected.cpp', 'cxa_vector.cpp',
        'cxa_virtual.cpp', 'exception.cpp', 'private_typeinfo.cpp',
        'stdexcept.cpp', 'typeinfo.cpp',
    }
    srcdir = root.path('src')
    libcxxabi = ctx.archive(
        srcdir.path(f).compile(
            ['-I../include', '-I../libunwind/include', '-std=c++11'])
        for f in sources)

    libcxxabi.install('lib/libc++abi.a')
    for f in {'include/cxxabi.h', 'include/__cxxabi_config.h'}:
        root.path(f).install(f)

package(
    name='libcxxabi',
    version='3.7.92',
    homepage='http://libcxxabi.llvm.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libcxx'},
    build_cmd=build,
)

distfile(
    name='libcxxabi-3.8.0rc2.src.tar.xz',
    checksum='d517b2f9b4dcf0cdf6bfd1d0417bd7ccd120d7f6d6a343d338f278be4e291d4c',
    master_sites={'http://llvm.org/pre-releases/3.8.0/rc2/'},
)
