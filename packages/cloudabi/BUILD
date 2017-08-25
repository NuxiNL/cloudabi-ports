# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.13',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.13.tar.gz',
    checksum='cf4c141e9cd89657114a4a4c326b682da471e86eedb829cfa48a2a568be00bb2',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
