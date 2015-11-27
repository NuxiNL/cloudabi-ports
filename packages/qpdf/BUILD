# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf(['--with-random='], inplace=True)
    build.make()
    build.make_install().install()

package(
    name='qpdf',
    version='6.0.0',
    homepage='http://qpdf.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'pcre', 'zlib'},
    build_cmd=build,
)

distfile(
    name='qpdf-6.0.0.tar.gz',
    checksum='a9fdc7e94d38fcd3831f37b6e0fe36492bf79aa6d54f8f66062cf7f9c4155233',
    master_sites=sites_sourceforge('qpdf/qpdf/6.0.0'),
)
