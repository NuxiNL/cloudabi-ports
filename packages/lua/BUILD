# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    srcdir.make(['posix'])
    srcdir.make(['install', 'INSTALL_TOP=%s/stage' % srcdir])
    srcdir.path('stage').install()

package(
    name='lua',
    version='5.3.3',
    homepage='http://www.lua.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='lua-5.3.3.tar.gz',
    checksum='5113c06884f7de453ce57702abaac1d618307f33f6789fa870e87a59d772aca2',
    master_sites={'http://www.lua.org/ftp/'},
    unsafe_string_sources={
        'src/lobject.c',
        'src/lstrlib.c',
    },
)
