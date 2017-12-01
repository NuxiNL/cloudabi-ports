# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure(['--with-random='], inplace=True)
    build.make()
    build.make_install().install()


package(
    name='qpdf',
    version='7.0.0',
    homepage='http://qpdf.sourceforge.net/',
    lib_depends={'c-runtime', 'jpeg', 'pcre', 'zlib'},
    build_cmd=build)

distfile(
    name='qpdf-7.0.0.tar.gz',
    checksum='fed08de14caad0fe5efd148d9eca886d812588b2cbb35d13e61993ee8eb8c65f',
    master_sites=sites_sourceforge('qpdf/qpdf/7.0.0'))
