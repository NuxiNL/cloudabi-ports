# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('libtom/ltp-0.04')
    root.make(['IGNORE_SPEED=yes', 'default'])
    root.make_install([
        'INCPATH=%s/include' % ctx.prefix(),
        'LIBPATH=%s/lib' % ctx.prefix(),
        'install',
    ]).install()

package(
    name='libtompoly',
    version='0.4',
    homepage='http://www.libtom.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libtommath'},
    build_cmd=build,
)

distfile(
    name='libtom/ltp-0.04.tar.bz2',
    checksum='6ce0d39caeda866b8f81029e8354efb9d5393850e78ea24f64475bd87b97fc0b',
    master_sites={'http://www.libtom.net/files/'},
)
