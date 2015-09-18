# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
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
    version='0.42.0',
    homepage='http://www.libtom.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libtom/ltm-0.42.0.tar.bz2',
    checksum='7b5c258304c34ac5901cfddb9f809b9b3b8ac7d04f700cf006ac766a923eb217',
    master_sites={'http://www.libtom.net/files/'},
)
