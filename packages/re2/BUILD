# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s/2016-05-01')
    root.make(['CXXFLAGS=-std=c++11 ' + ctx.cxxflags()])
    root.make_install(['prefix=' + ctx.prefix(), 'install']).install()

package(
    name='re2',
    version='0.20160501',
    homepage='https://github.com/google/re2',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='re2/2016-05-01.tar.gz',
    checksum='d9d13f0ea4e1c6628b1cb85eeee284d4fdd4948da94b1f205096254927092e3d',
    master_sites={'https://github.com/google/re2/archive/'},
    unsafe_string_sources={'util/strutil.cc'},
)
