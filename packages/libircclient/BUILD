# Copyright (c) 2017 Sjors Gielen
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(
        ['ac_cv_func_malloc_0_nonnull=yes'], inplace=True)
    build.make()
    build.make_install().install()


package(
    name='libircclient',
    version='1.9',
    homepage='https://sourceforge.net/p/libircclient',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='libircclient-1.9.tar.gz',
    checksum='81c397eee618667bccfe8960352ba5f829c8c2e9badc270594b91128cd89c064',
    master_sites=sites_sourceforge('libircclient/libircclient/1.9'),
    unsafe_string_sources={
        'src/libircclient.c', 'src/colors.c', 'src/utils.c'
    })
