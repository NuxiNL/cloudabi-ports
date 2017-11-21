# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.18',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.18.tar.gz',
    checksum='923c09572718ce320c93eda0458f47420df894f179cc0b174880d6e23060aaaf',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
