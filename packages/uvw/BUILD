# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s_libuv-v1.15').path('src')
    for i in {'fs', 'fs_event', 'fs_poll', 'lib', 'signal', 'tty', 'udp'}:
        srcdir.path('uvw').path(i + '.hpp').remove()

    # Test whether this library can actually be included and used.
    ctx.resource('compile-test.cc').compile([
        '-I%s' % srcdir,
        '-std=c++14',
    ])

    srcdir.install('include')


package(
    name='uvw',
    version='1.3.0',
    homepage='https://github.com/skypjack/uvw',
    lib_depends={'libcxx'},
    build_cmd=build)

distfile(
    name='uvw/v1.3.0_libuv-v1.15.tar.gz',
    checksum='9b4107915d857475b9557e40fe58f23d0a516a3be4ce04f7c97ae3790bded371',
    master_sites={'https://github.com/skypjack/uvw/archive/'})
