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
        'algorithm.cpp',
        'any.cpp',
        'bind.cpp',
        'chrono.cpp',
        'condition_variable.cpp',
        'debug.cpp',
        'exception.cpp',
        'experimental/memory_resource.cpp',
        'functional.cpp',
        'future.cpp',
        'hash.cpp',
        'ios.cpp',
        'iostream.cpp',
        'locale.cpp',
        'memory.cpp',
        'mutex.cpp',
        'new.cpp',
        'optional.cpp',
        'random.cpp',
        'regex.cpp',
        'shared_mutex.cpp',
        'stdexcept.cpp',
        'string.cpp',
        'strstream.cpp',
        'system_error.cpp',
        'thread.cpp',
        'typeinfo.cpp',
        'utility.cpp',
        'valarray.cpp',
        'variant.cpp',
        'vector.cpp',
    }
    srcdir = root.path('src')
    libcxx = ctx.archive(
        srcdir.path(f).compile([
            '-I%s/include' % root,
            '-I%s/include' % cxxabi,
            '-std=c++11',
            '-D_LIBCPP_BUILD_STATIC',
            '-D_LIBCPP_BUILDING_LIBRARY',
            '-DLIBCXX_BUILDING_LIBCXXABI',
        ]) for f in sources)
    libcxx.install('lib/libc++.a')


package(
    name='libcxx',
    version='5.0.0',
    homepage='http://libcxx.llvm.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libcxx-5.0.0.src.tar.xz',
    checksum='eae5981e9a21ef0decfcac80a1af584ddb064a32805f95a57c7c83a5eb28c9b1',
    master_sites={'http://releases.llvm.org/5.0.0/'})
