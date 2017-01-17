# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.9',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.9.tar.gz',
    checksum='88f3d5e374f4b605c26ab09c9e5396ae573e1a634a642f76b9b626e1d4c0f78a',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
