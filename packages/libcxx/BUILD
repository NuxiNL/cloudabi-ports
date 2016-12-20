# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    cxxabi = ctx.extract('libcxxabi-%(version)s.src')

    # Install header files.
    headers = root.path('include')
    headers.path('CMakeLists.txt').remove()
    headers.path('experimental/filesystem').remove()
    headers.path('support').remove()
    headers.install('include/c++/v1')

    # Build libc++.a.
    sources = {
        'algorithm.cpp', 'any.cpp', 'bind.cpp', 'chrono.cpp',
        'condition_variable.cpp', 'debug.cpp', 'exception.cpp',
        'experimental/memory_resource.cpp', 'future.cpp', 'hash.cpp',
        'ios.cpp', 'iostream.cpp', 'locale.cpp', 'memory.cpp',
        'mutex.cpp', 'new.cpp', 'optional.cpp', 'random.cpp',
        'regex.cpp', 'shared_mutex.cpp', 'stdexcept.cpp', 'string.cpp',
        'strstream.cpp', 'system_error.cpp', 'thread.cpp',
        'typeinfo.cpp', 'utility.cpp', 'valarray.cpp',
    }
    srcdir = root.path('src')
    libcxx = ctx.archive(
        srcdir.path(f).compile([
            '-I%s/include' % root, '-I%s/include' % cxxabi,
            '-std=c++11', '-D_LIBCPP_BUILD_STATIC',
            '-DLIBCXX_BUILDING_LIBCXXABI',
        ]) for f in sources)
    libcxx.install('lib/libc++.a')

package(
    name='libcxx',
    version='3.9.0',
    homepage='http://libcxx.llvm.org/',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libcxx-3.9.0.src.tar.xz',
    checksum='d0b38d51365c6322f5666a2a8105785f2e114430858de4c25a86b49f227f5b06',
    master_sites={'http://llvm.org/releases/3.9.0/'},
)
