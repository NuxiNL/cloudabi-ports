# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    library = ctx.archive([srcdir.path('http_parser.c').compile()])
    library.install('lib/libhttp_parser.a')
    srcdir.path('http_parser.h').install('include/http_parser.h')


package(
    name='http-parser',
    version='2.7.1',
    homepage='https://github.com/nodejs/http-parser',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='http-parser/v2.7.1.tar.gz',
    checksum='70409ad324e5de2da6a0f39e859e566d497c1ff0a249c0c38a5012df91b386b3',
    master_sites={'https://github.com/nodejs/http-parser/archive/'})
