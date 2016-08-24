# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-3.9.0rc2.src')
    cxxabi = ctx.extract('libcxxabi-3.9.0rc2.src')

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
    version='3.8.92',
    homepage='http://libcxx.llvm.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libcxx-3.9.0rc2.src.tar.xz',
    checksum='3bda7b35226efaa7616cfc3dd23f147c89a7b6565553e9fc9907d434aa013560',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc2/'},
)
