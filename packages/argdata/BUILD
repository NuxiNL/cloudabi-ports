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
    version='0.5',
    homepage='https://github.com/NuxiNL/argdata',
    lib_depends={'cloudlibc', 'libcxx', 'mstd'},
    build_cmd=build)

distfile(
    name='argdata/v0.5.tar.gz',
    checksum='8e1b92bb6dd1cf5f3fefcaf58e1a9d7c7caa8f255e85008ea79150a86319727d',
    master_sites={'https://github.com/NuxiNL/argdata/archive/'})
