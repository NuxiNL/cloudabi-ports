# Copyright (c) 2015-2019 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.21',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.21.tar.gz',
    checksum='f76efd4ca2774659c4c4032b80ab639653a665908ace53a50ab4926126d103b5',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
