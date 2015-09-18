# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('libtom/tfm-%(version)s')
    root.make(['IGNORE_SPEED=yes', 'default'])
    root.make_install([
        'INCPATH=%s/include' % ctx.prefix(),
        'LIBPATH=%s/lib' % ctx.prefix(),
        'install',
    ]).install()

package(
    name='tomsfastmath',
    version='0.12',
    homepage='http://www.libtom.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libtom/tfm-0.12.tar.bz2',
    checksum='aa854c6664c3ba173809326ad9d3c18918b52f84040658b247e2ce7527032021',
    master_sites={'http://www.libtom.net/files/'},
)
