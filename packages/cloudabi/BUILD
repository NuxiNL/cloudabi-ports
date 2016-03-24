# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.1',
    homepage='https://github.com/NuxiNL/cloudabi',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.1.tar.gz',
    checksum='b7ba7d066942b68821e57210ced53e94db99b4ee679436d38a4d3021c6010eac',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
