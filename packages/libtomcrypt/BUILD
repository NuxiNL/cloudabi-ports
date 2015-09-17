# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.

def build(ctx):
    root = ctx.extract('libtom/crypt-%(version)s')
    root.make(['IGNORE_SPEED=yes', 'default'])
    root.make_install([
        'INCPATH=%s/include' % ctx.prefix(),
        'LIBPATH=%s/lib' % ctx.prefix(),
        'NODOCS=yes',
        'install',
    ]).install()

package(
    name='libtomcrypt',
    version='1.17',
    homepage='http://www.libtom.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libtom/crypt-1.17.tar.bz2',
    checksum='e33b47d77a495091c8703175a25c8228aff043140b2554c08a3c3cd71f79d116',
    master_sites={'http://www.libtom.net/files/'},
    patches={'clang', 'makefile', 'no-fopen'},
)
