# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')


package(
    name='cloudabi',
    version='0.12',
    homepage='https://github.com/NuxiNL/cloudabi',
    build_cmd=build)

distfile(
    name='cloudabi/v0.12.tar.gz',
    checksum='e3e9b4045ce9cdece50252107c0b9156c39ce723586cafba5ddb569aa34d2844',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'})
