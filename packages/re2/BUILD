# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s/2017-03-01')
    root.make(['CXXFLAGS=-std=c++11 ' + ctx.cxxflags()])
    root.make_install(['prefix=' + ctx.prefix(), 'install']).install()

package(
    name='re2',
    version='0.20170301',
    homepage='https://github.com/google/re2',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='re2/2017-03-01.tar.gz',
    checksum='19db0b87bdc22e7e4c66af17f3170167a1b9cb9e32fd6b26189157f1336b73e8',
    master_sites={'https://github.com/google/re2/archive/'},
    unsafe_string_sources={'util/strutil.cc'},
)
