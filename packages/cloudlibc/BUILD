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
    version='0.9',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudlibc-0.9.tar.xz',
    checksum='20933b4b95f53abd6e16db792f4d4ea87fbea66946e17c641d2cf5baeea3a131',
    master_sites={'https://nuxi.nl/distfiles/cloudlibc/'},
)
