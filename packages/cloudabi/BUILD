# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.7',
    homepage='https://github.com/NuxiNL/cloudabi',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.7.tar.gz',
    checksum='a6e9fc8aa8c9ca70be5842e8097b4f260461ad2d00c683d84df88c6eb54caa52',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
