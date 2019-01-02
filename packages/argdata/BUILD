# Copyright (c) 2017-2019 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    # As cloudlibc already includes a copy of argdata, only use this
    # package to install the C++ header file.
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('src/argdata.hpp').install('include/argdata.hpp')


package(
    name='argdata',
    version='0.8',
    homepage='https://github.com/NuxiNL/argdata',
    lib_depends={'cloudlibc', 'libcxx'},
    build_cmd=build)

distfile(
    name='argdata/v0.8.tar.gz',
    checksum='b6e940948305a741f285df8ba8534ef05726c1263768a291fdb46fd3aff5afd6',
    master_sites={'https://github.com/NuxiNL/argdata/archive/'})
