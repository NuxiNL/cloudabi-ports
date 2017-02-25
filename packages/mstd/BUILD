# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/%(version)s').path('include').install('include')

package(
    name='mstd',
    version='1',
    homepage='https://github.com/m-ou-se/mstd',
    lib_depends={'libcxx'},
    build_cmd=build,
)

distfile(
    name='mstd/1.tar.gz',
    checksum='9d4c124ec9962d11cd206f21e9e349801e97f8374c613c403a3d853cb8fe378e',
    master_sites={'https://github.com/m-ou-se/mstd/archive/'},
)
