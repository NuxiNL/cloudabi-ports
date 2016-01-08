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
    version='0.17',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudlibc-0.17.tar.xz',
    checksum='14f8aa21aee577abfca3a474f41c35a77c8d5d44659d861e6b2b3747d7a08b04',
    master_sites={'https://nuxi.nl/distfiles/cloudlibc/'},
)
