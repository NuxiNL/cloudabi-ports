# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)s-0.15.1b').autoconf()
    build.make()
    build.make_install().install()

package(
    name='libid3tag',
    version='0.15.1.2',
    homepage='http://www.underbit.com/products/mad/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='libid3tag-0.15.1b.tar.gz',
    checksum='63da4f6e7997278f8a3fef4c6a372d342f705051d1eeb6a46a86b03610e26151',
    master_sites=sites_sourceforge('mad/libid3tag/0.15.1b'),
)
