# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.2',
    homepage='https://github.com/NuxiNL/cloudabi',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.2.tar.gz',
    checksum='a134d52cb6cc4d1aae67ae0f5877b4dc83c13b3d9b3e1cdd0ac34b5be295ebf2',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
