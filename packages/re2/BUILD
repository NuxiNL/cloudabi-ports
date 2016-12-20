# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s/2016-10-01')
    root.make(['CXXFLAGS=-std=c++11 ' + ctx.cxxflags()])
    root.make_install(['prefix=' + ctx.prefix(), 'install']).install()

package(
    name='re2',
    version='0.20161001',
    homepage='https://github.com/google/re2',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='re2/2016-10-01.tar.gz',
    checksum='11fd87507450fe2bbdcdb3971ea2e0bedd71a02f064118ef1ac60aa6ac85992d',
    master_sites={'https://github.com/google/re2/archive/'},
    unsafe_string_sources={'util/strutil.cc'},
)
