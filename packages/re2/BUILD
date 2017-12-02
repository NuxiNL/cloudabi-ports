# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract('%(name)s/2017-11-01')
    root.make(['CXXFLAGS=-std=c++11 ' + ctx.cxxflags()])
    root.make_install(['prefix=' + ctx.prefix(), 'install']).install()


package(
    name='re2',
    version='0.20171101',
    homepage='https://github.com/google/re2',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='re2/2017-11-01.tar.gz',
    checksum='0a6d5035c55dde5aca9cd15026671e183b4083451da474e06aba449cf9101765',
    master_sites={'https://github.com/google/re2/archive/'},
    unsafe_string_sources={'util/strutil.cc'})
