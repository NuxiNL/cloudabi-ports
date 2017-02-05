# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.10',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.10.tar.gz',
    checksum='b425e111cbb8bea75069c46a3bd7c8ddb7b0adbf87af3fa5bb927f779eaa6e34',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
