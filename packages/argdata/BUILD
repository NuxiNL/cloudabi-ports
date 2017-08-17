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
    version='0.6',
    homepage='https://github.com/NuxiNL/argdata',
    lib_depends={'cloudlibc', 'libcxx'},
    build_cmd=build)

distfile(
    name='argdata/v0.6.tar.gz',
    checksum='15983371932190f7488c5e0a597bc4c2510c35ed336cbbfb3407d78e2fbc303e',
    master_sites={'https://github.com/NuxiNL/argdata/archive/'})
