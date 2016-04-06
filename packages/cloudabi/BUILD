# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    ctx.extract('%(name)s/v%(version)s').path('headers').install('include')

package(
    name='cloudabi',
    version='0.3',
    homepage='https://github.com/NuxiNL/cloudabi',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cloudabi/v0.3.tar.gz',
    checksum='cb1d793d31efb2a5c17a96f363931c3a4ddf9879e977d27eaeb814732227df71',
    master_sites={'https://github.com/NuxiNL/cloudabi/archive/'},
)
