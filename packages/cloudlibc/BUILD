# Copyright (c) 2015 Nuxi, https://nuxi.nl/
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
    version='0.14',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudlibc-0.14.tar.xz',
    checksum='fea205dbf77cb5e88551020715b451f5f9b9c23c9e2b12c8a047ad101a152705',
    master_sites={'https://nuxi.nl/distfiles/cloudlibc/'},
)
