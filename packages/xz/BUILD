# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure([
        '--disable-lzmadec',
        '--disable-lzmainfo',
        '--disable-scripts',
        '--disable-xz',
        '--disable-xzdec',

        # Work around an issue on FreeBSD, where libmd's SHA256
        # functions causes checksum failures.
        'ac_cv_type_SHA256_CTX=no',
        'ac_cv_search_SHA256_Init=no',
    ])
    build.make()
    build.make_install().install()


package(
    name='xz',
    version='5.2.3',
    homepage='http://tukaani.org/xz/',
    lib_depends={'c-runtime'},
    build_cmd=build)

host_package(
    name='xz',
    version='5.2.3',
    homepage='http://tukaani.org/xz/',
    build_cmd=build)

distfile(
    name='xz-5.2.3.tar.xz',
    checksum='7876096b053ad598c31f6df35f7de5cd9ff2ba3162e5a5554e4fc198447e0347',
    master_sites={'http://tukaani.org/xz/'})
