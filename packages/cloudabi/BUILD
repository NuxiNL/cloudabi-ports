# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.17',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.17.tar.gz',
    checksum='bf89c61ca22fcf36db3b2373bc4e0618540362795bffacf29e88c7f4e3ef267a',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
