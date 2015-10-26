# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    ctx.archive({
        srcdir.path('picosat.c').compile(['-DNGETRUSAGE'])
    }).install('lib/libpicosat.a')
    srcdir.path('picosat.h').install('include/picosat.h')

package(
    name='picosat',
    version='960',
    homepage='http://fmv.jku.at/picosat/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='picosat-960.tar.gz',
    checksum='edb3184a04766933b092713d0ae5782e4a3da31498629f8bb2b31234a563e817',
    master_sites={'http://fmv.jku.at/picosat/'},
)
