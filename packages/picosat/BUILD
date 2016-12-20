# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    ctx.archive({
        srcdir.path('picosat.c').compile()
    }).install('lib/libpicosat.a')
    srcdir.path('picosat.h').install('include/picosat.h')

package(
    name='picosat',
    version='965',
    homepage='http://fmv.jku.at/picosat/',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='picosat-965.tar.gz',
    checksum='15169b4f28ba8f628f353f6f75a100845cdef4a2244f101a02b6e5a26e46a754',
    master_sites={'http://fmv.jku.at/picosat/'},
    unsafe_string_sources={'picosat.c'},
)
