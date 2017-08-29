# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.14',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.14.tar.gz',
    checksum='9bea06fabf88810e4725696e8e2ba7ec790f2c3ed49929050b07e3d7af07398c',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
