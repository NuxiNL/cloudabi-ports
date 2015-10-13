# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    root.run(['./build'])

    root.run(['DESTDIR=stage', 'PREFIX=/', './install'])
    root.path('stage').install()

package(
    name='cloudlibc',
    version='0.8',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudlibc-0.8.tar.xz',
    checksum='d296d779fe8ef8d46210f9cc67406250251a69d839c85d4b764ec6d5f948a06f',
    master_sites={'https://nuxi.nl/distfiles/cloudlibc/'},
)
