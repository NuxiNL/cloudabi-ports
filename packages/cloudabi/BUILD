# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.8',
    homepage='https://github.com/NuxiNL/cloudabi',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.8.tar.gz',
    checksum='dcde2eefad9ba3a56063e0c8af369f806ff16671a1a54d6a7d1d506031263ac8',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
