# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)ssrc.v9a').autoconf()
    build.make(['bin_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'man_MANS=', 'install']).install()

package(
    name='jpeg',
    version='9.1',
    homepage='http://www.ijg.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='jpegsrc.v9a.tar.gz',
    checksum='3a753ea48d917945dd54a2d97de388aa06ca2eb1066cbfdc6652036349fe05a7',
    master_sites={'http://www.ijg.org/files/'},
    patches={'no-sprintf'},
)
