# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
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
    version='0.76',
    homepage='https://github.com/NuxiNL/cloudlibc',
    lib_depends={'cloudabi', 'compiler-rt'},
    build_cmd=build,
)

distfile(
    name='cloudlibc/v0.76.tar.gz',
    checksum='f808148aeb4062de9a2f7482188313cbeaee119124d22a3e66981f4658ab50cb',
    master_sites={'https://github.com/NuxiNL/cloudlibc/archive/'},
)
