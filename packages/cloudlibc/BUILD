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
    version='0.15',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudlibc-0.15.tar.xz',
    checksum='b4ab5f0a5c6496ec0213a145dc5d19e5eb1ea8168ddcfd16481dc2e11fec61c3',
    master_sites={'https://nuxi.nl/distfiles/cloudlibc/'},
)
