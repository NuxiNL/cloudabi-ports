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
    version='0.52',
    homepage='https://github.com/NuxiNL/cloudlibc',
    maintainer='info@nuxi.nl',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build,
)

distfile(
    name='cloudlibc/v0.52.tar.gz',
    checksum='8f80e903b2c3edbaca818d908ec03543d7b1e9815d4dfd5217d9529a931dc8ef',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'},
)
