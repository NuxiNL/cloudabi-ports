# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)s-1.2rc3').gnu_configure([
        '--disable-examples', '--disable-neon',
    ])
    build.make()
    build.make_install().install()

package(
    name='speexdsp',
    version='1.1.93',
    homepage='http://www.speex.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='speexdsp-1.2rc3.tar.gz',
    checksum='4ae688600039f5d224bdf2e222d2fbde65608447e4c2f681585e4dca6df692f1',
    master_sites={'http://downloads.xiph.org/releases/speex/'},
)
