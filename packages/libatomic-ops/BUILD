# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract('libatomic_ops-%(version)s').gnu_configure()
    build.make()
    build.make_install().install()


package(
    name='libatomic-ops',
    version='7.4.0',
    homepage='http://www.hpl.hp.com/research/linux/atomic_ops/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libatomic_ops-7.4.0.tar.gz',
    checksum='2875ccc29254d3375dab9c5930c42df342f148f8cd7c646621dbf03f8c1d5b5a',
    master_sites={'http://www.hpl.hp.com/research/linux/atomic_ops/download/'},
)
