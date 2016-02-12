# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('libtom/ltf-0.02')
    root.make(['IGNORE_SPEED=yes', 'default'])
    root.make_install([
        'INCPATH=%s/include' % ctx.prefix(),
        'LIBPATH=%s/lib' % ctx.prefix(),
        'install',
    ]).install()

package(
    name='libtomfloat',
    version='0.2',
    homepage='http://www.libtom.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libtommath'},
    build_cmd=build,
)

distfile(
    name='libtom/ltf-0.02.tar.bz2',
    checksum='7e80498e526888e3999cb711bd9b2ffc6738723adb89c7dd400f133b46a88707',
    master_sites={'https://github.com/libtom/libtomfloat/releases/download/0.02/'},
)
