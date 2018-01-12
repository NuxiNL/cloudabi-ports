# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.19',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.19.tar.gz',
    checksum='d78947e52d45f2202469b3606d2171b9f5e26258067d6d76f41e3e80c2555ff3',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
