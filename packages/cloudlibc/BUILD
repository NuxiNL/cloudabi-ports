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
    version='0.75',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build,
)

distfile(
    name='cloudlibc/v0.75.tar.gz',
    checksum='7f28d7d4b47d8a0dc61f577a6577aa706b66e85e78c05c6c450d60274aa3cf2f',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'},
)
