# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    srcdir.make(['posix'])
    srcdir.make(['install', 'INSTALL_TOP=%s/stage' % srcdir])
    srcdir.path('stage').install()

package(
    name='lua',
    version='5.3.1',
    homepage='http://www.lua.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='lua-5.3.1.tar.gz',
    checksum='072767aad6cc2e62044a66e8562f51770d941e972dc1e4068ba719cd8bffac17',
    master_sites={'http://www.lua.org/ftp/'},
)
