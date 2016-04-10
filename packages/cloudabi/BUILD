# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.4',
    homepage='https://github.com/NuxiNL/cloudabi',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.4.tar.gz',
    checksum='c0ab8d2987e95d1db1cca84062ed43ed4fe13533d646e2830106da2eaeee87e9',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
