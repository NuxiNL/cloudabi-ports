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
    version='0.22',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    lib_depends={'compiler-rt'},
    build_cmd=build,
)

distfile(
    name='cloudlibc-0.22.tar.xz',
    checksum='82de83621595fcb893de20dfcd6342f6d5591b35f9bccb42702add5342330da7',
    master_sites={'https://nuxi.nl/distfiles/cloudlibc/'},
)
