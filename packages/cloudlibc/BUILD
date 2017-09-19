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
    version='0.84',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build)

distfile(
    name='cloudlibc/v0.84.tar.gz',
    checksum='1c87064f37c1bd3c401ee1491288ff12e402b09c99f253caf638791e99591013',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'})
