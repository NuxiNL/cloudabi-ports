# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


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
    version='0.13.1',
    homepage='http://www.libtom.net/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libtom/tfm-0.13.1.tar.xz',
    checksum='47c97a1ada3ccc9fcbd2a8a922d5859a84b4ba53778c84c1d509c1a955ac1738',
    master_sites={
        'https://github.com/libtom/tomsfastmath/releases/download/v0.13.1/'
    },
    unsafe_string_sources={'src/misc/fp_ident.c'})
