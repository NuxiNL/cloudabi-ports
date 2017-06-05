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
    version='0.3',
    homepage='https://github.com/NuxiNL/argdata',
    lib_depends={'cloudlibc', 'libcxx', 'mstd'},
    build_cmd=build,
)

distfile(
    name='argdata/v0.3.tar.gz',
    checksum='12e3cc43074e2d7b22a4ae81e7262c932a4b8144b5b03f59578c00aa8aea16f4',
    master_sites={'https://github.com/NuxiNL/argdata/archive/'},
)
