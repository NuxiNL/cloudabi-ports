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
    version='0.1',
    homepage='https://github.com/NuxiNL/argdata',
    lib_depends={'cloudlibc', 'libcxx', 'mstd'},
    build_cmd=build,
)

distfile(
    name='argdata/v0.1.tar.gz',
    checksum='1fd26745e72382b9e0eda042154b3219682de980f6cdd15f574f9d4288b7df79',
    master_sites={'https://github.com/NuxiNL/argdata/archive/'},
)
