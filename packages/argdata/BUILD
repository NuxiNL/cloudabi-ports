# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    # As cloudlibc already includes a copy of argdata, only use this
    # package to install the C++ header file.
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('src/argdata.hpp').install('include/argdata.hpp')


package(
    name='argdata',
    version='0.7',
    homepage='https://github.com/NuxiNL/argdata',
    lib_depends={'cloudlibc', 'libcxx'},
    build_cmd=build)

distfile(
    name='argdata/v0.7.tar.gz',
    checksum='ed48e65c9e4d1ee0d3d72adee9d7a64690e2afd15e0e4eec799ddf409f89799c',
    master_sites={'https://github.com/NuxiNL/argdata/archive/'})
