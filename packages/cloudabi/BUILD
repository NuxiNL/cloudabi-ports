# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.11',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.11.tar.gz',
    checksum='f70d6b6e2e9dfd3f32015a18806bd625dbbad4480db65d4a771cb92abe961d13',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
