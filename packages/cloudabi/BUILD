# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.15',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.15.tar.gz',
    checksum='c4dbb8a1c53597cfb0ef1645c1fcd2bbcef91cbfc95cc2e4b2740e5cb42f28f4',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
