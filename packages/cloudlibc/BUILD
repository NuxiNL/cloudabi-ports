# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s/v%(version)s')
    root.run(['./build'])

    root.run(['DESTDIR=stage', 'PREFIX=/', './install'])
    root.path('stage').install()

package(
    name='cloudlibc',
    version='0.70',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build,
)

distfile(
    name='cloudlibc/v0.70.tar.gz',
    checksum='a1fe46e3060811ffb367cfa2d26bdb6dd984c803a3cb42763032b0fcf67fa8a4',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'},
)
