# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
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
    version='0.13',
    homepage='http://www.libtom.net/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libtom/tfm-0.13.tar.bz2',
    checksum='8defe6f20759a455ade46b2f3c4de46d2358a6222236f78012736a6aeed63407',
    master_sites={
        'https://github.com/libtom/tomsfastmath/releases/download/v0.13.0/'
    },
    unsafe_string_sources={'src/misc/fp_ident.c'})
