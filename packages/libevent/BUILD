# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract('%(name)s-%(version)s-stable').gnu_configure()
    build.make()
    build.make_install().install()


package(
    name='libevent',
    version='2.0.22',
    homepage='http://libevent.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libevent-2.0.22-stable.tar.gz',
    checksum='71c2c49f0adadacfdbe6332a372c38cf9c8b7895bb73dabeaa53cdcc1d4e1fa3',
    master_sites={
        'https://github.com/libevent/libevent/releases/download/release-2.0.22-stable/'
    })
