# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.6',
    homepage='https://github.com/NuxiNL/cloudabi',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.6.tar.gz',
    checksum='2b3e1ad30e4af3d2cb5560fb25d2bc9d328db7d1ad1f648dbd4bb8dbb3effb50',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
