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
    version='0.77',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build,
)

distfile(
    name='cloudlibc/v0.77.tar.gz',
    checksum='4d11efa8b1f32a9e29ba7ba4aa89041d9870b291750475d82fbfda784e37d8e5',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'},
)
