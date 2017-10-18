# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.16',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.16.tar.gz',
    checksum='a1eebcc716019178e04d206f854a01335ed1aab75f8da1a8ca02aebca7f125ad',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
