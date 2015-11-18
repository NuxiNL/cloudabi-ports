# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)s-0.15.1b').autoconf()
    build.make()
    build.make_install().install()

package(
    name='libmad',
    version='0.15.1.2',
    homepage='http://www.underbit.com/products/mad/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libmad-0.15.1b.tar.gz',
    checksum='bbfac3ed6bfbc2823d3775ebb931087371e142bb0e9bb1bee51a76a6e0078690',
    master_sites=sites_sourceforge('mad/libmad/0.15.1b'),
    unsafe_string_sources={'timer.c'},
)
