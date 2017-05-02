# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/%(version)s').path('include').install('include')

package(
    name='mstd',
    version='1.1',
    homepage='https://github.com/m-ou-se/mstd',
    lib_depends={'libcxx'},
    build_cmd=build,
)

distfile(
    name='mstd/1.1.tar.gz',
    checksum='5130a8dfbcbf57c0807d9ccfb1cfadc1334252a4fb7810f635dd033aac4714f5',
    master_sites={'https://github.com/m-ou-se/mstd/archive/'},
)
