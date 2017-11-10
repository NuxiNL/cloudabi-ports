# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract('%(name)s/de0b0f43951321adbbf1231afc71e7dcab08d388')

    # Install header files.
    root.path('include').install('include')

    # Build libcppcoro.
    sources = {
        'async_auto_reset_event.cpp', 'async_manual_reset_event.cpp',
        'async_mutex.cpp', 'cancellation_state.cpp', 'cancellation_token.cpp',
        'cancellation_source.cpp', 'cancellation_registration.cpp',
        'lightweight_manual_reset_event.cpp'
    }
    srcdir = root.path('lib')
    libcppcoro = ctx.archive(
        srcdir.path(f).compile([
            '-I%s/include' % root,
            '-std=c++1z',
            '-fcoroutines-ts',
        ]) for f in sources)
    libcppcoro.install('lib/libcppcoro.a')


package(
    name='cppcoro',
    version='0.0.20170824',
    homepage='https://github.com/lewissbaker/cppcoro',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='cppcoro/de0b0f43951321adbbf1231afc71e7dcab08d388.tar.gz',
    checksum='7d98a234fde4110fdd708f553f785e4b668b49e3bcedf30457f3343b447a5a69',
    master_sites={'https://github.com/lewissbaker/cppcoro/archive/'})
