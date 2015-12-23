# Copyright (c) 2015 Nuxi, https://nuxi.nl/
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
    version='5.3.2',
    homepage='http://www.lua.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='lua-5.3.2.tar.gz',
    checksum='c740c7bb23a936944e1cc63b7c3c5351a8976d7867c5252c8854f7b2af9da68f',
    master_sites={'http://www.lua.org/ftp/'},
    unsafe_string_sources={
        'src/lobject.c',
        'src/lstrlib.c',
    },
)
