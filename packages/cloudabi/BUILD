# Copyright (c) 2015-2018 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.20',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.20.tar.gz',
    checksum='454076b8f7ffb536004c65970246fdfbc5b60abaead938583a269bb6bd81d6e6',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
