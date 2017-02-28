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
    version='0.2',
    homepage='https://github.com/NuxiNL/argdata',
    lib_depends={'cloudlibc', 'libcxx', 'mstd'},
    build_cmd=build,
)

distfile(
    name='argdata/v0.2.tar.gz',
    checksum='bfc97e8a8a0d34909f2627e80013f2c3da2492e7b86060636a5d46731c12aee0',
    master_sites={'https://github.com/NuxiNL/argdata/archive/'},
)
