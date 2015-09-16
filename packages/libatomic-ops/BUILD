# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('libatomic_ops-%(version)s').autoconf()
    build.make()
    build.make_install().install()

package(
    name='libatomic-ops',
    version='7.4.0',
    homepage='http://www.hpl.hp.com/research/linux/atomic_ops/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libatomic_ops-7.4.0.tar.gz',
    checksum='2875ccc29254d3375dab9c5930c42df342f148f8cd7c646621dbf03f8c1d5b5a',
    master_sites={'http://www.hpl.hp.com/research/linux/atomic_ops/download/'},
    patches={'use-no-signals'},
)
