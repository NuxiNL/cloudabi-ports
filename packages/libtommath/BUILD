# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('libtom/ltm-%(version)s')
    root.make(['IGNORE_SPEED=yes', 'default'])
    root.make_install([
        'INCPATH=%s/include' % ctx.prefix(),
        'LIBPATH=%s/lib' % ctx.prefix(),
        'install',
    ]).install()

package(
    name='libtommath',
    version='1.0',
    homepage='http://www.libtom.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libtom/ltm-1.0.tar.xz',
    checksum='993a7df9ee091fca430cdde3263df57d88ef62af8103903214da49fc51bbb56c',
    master_sites={'https://github.com/libtom/libtommath/releases/download/v1.0/'},
)
