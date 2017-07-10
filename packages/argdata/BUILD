# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # As cloudlibc already includes a copy of argdata, only use this
    # package to install the C++ header file.
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('src/argdata.hpp').install('include/argdata.hpp')


package(
    name='argdata',
    version='0.4',
    homepage='https://github.com/NuxiNL/argdata',
    lib_depends={'cloudlibc', 'libcxx', 'mstd'},
    build_cmd=build)

distfile(
    name='argdata/v0.4.tar.gz',
    checksum='8f7afec1c3d832cd559865a8125d47edf70b4368d2e97f79bc36473090378fae',
    master_sites={'https://github.com/NuxiNL/argdata/archive/'})
