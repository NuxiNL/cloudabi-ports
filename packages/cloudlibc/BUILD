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
    version='0.5',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudlibc-0.5.tar.xz',
    checksum='9cff70a377973dc3958f942812bb0fe920692d8bf432edf4dd351214cb0f565b',
    master_sites={'https://nuxi.nl/distfiles/cloudlibc/'},
)
