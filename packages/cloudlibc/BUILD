# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
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
    version='0.22',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    lib_depends={'compiler-rt'},
    build_cmd=build,
)

distfile(
    name='cloudlibc/v0.22.tar.gz',
    checksum='8f6b8c3c28f03cf066eae36b92c1e2fa8e974a618e7a13809cc7c630dccabd65',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'},
)
