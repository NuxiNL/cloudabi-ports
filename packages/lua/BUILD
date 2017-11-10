# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract()
    srcdir.make(['posix'])
    srcdir.make(['install', 'INSTALL_TOP=%s/stage' % srcdir])
    srcdir.path('stage').install()


package(
    name='lua',
    version='5.3.4',
    homepage='http://www.lua.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='lua-5.3.4.tar.gz',
    checksum='f681aa518233bc407e23acf0f5887c884f17436f000d453b2491a9f11a52400c',
    master_sites={'http://www.lua.org/ftp/'},
    unsafe_string_sources={
        'src/lobject.c',
        'src/lstrlib.c',
    })
