# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    root.run(['./build'])

    root.run(['DESTDIR=stage', 'PREFIX=/', './install'])
    root.path('stage').install()

package(
    name='cloudlibc',
    version='0.21',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    lib_depends={'compiler-rt'},
    build_cmd=build,
)

distfile(
    name='cloudlibc-0.21.tar.xz',
    checksum='21b233352f9964e2aa7de4b04633ea5eca17228e9f5f128b2ab81b8fbe3f4457',
    master_sites={'https://nuxi.nl/distfiles/cloudlibc/'},
)
