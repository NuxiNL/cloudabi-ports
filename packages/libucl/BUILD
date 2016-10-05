# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/%(version)s')
    srcdir.autoreconf()
    build = srcdir.gnu_configure(['--enable-signatures'])
    build.make()
    build.make_install().install()

package(
    name='libucl',
    version='0.8.0',
    homepage='https://github.com/vstakhov/libucl',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libressl'},
    build_cmd=build,
)

distfile(
    name='libucl/0.8.0.tar.gz',
    checksum='af361cd1f0b7b66c228a1c04a662ccaa9ee8af79842046c04446d915db349ee1',
    master_sites={'https://github.com/vstakhov/libucl/archive/'},
)
