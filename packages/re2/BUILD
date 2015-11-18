# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s/2015-11-01')
    root.make()
    root.make_install(['prefix=' + ctx.prefix(), 'install']).install()

package(
    name='re2',
    version='0.20151101',
    homepage='https://github.com/google/re2',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='re2/2015-11-01.tar.gz',
    checksum='4aeca04541b63af1e38682b20440fcde2207a4a8a04466359dd113c8a7d4657e',
    master_sites={'https://github.com/google/re2/archive/'},
    unsafe_string_sources={'util/strutil.cc'},
)
