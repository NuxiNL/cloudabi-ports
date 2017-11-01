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
    version='0.92',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build)

distfile(
    name='cloudlibc/v0.92.tar.gz',
    checksum='b82cfbfb5663aa0477d2a1aad4452a92577531a419e92d1617a83b877ceab42e',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'})
