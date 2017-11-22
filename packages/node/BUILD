# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/f722d3122cd0c3d4a03bb2fb73998d6087e8318a')
    srcdir.run([
        'python2',
        './configure',
        '--dest-os=cloudabi',
        '--shared-cares',
        '--shared-http-parser',
        '--shared-libuv',
        '--shared-nghttp2',
        '--shared-zlib',
        '--with-intl=system-icu',
        '--without-inspector',
        '--without-node-options',
        '--without-snapshot',
        '--without-ssl',
    ])
    srcdir.make()
    srcdir.make_install(['PREFIX=' + ctx.prefix(), 'install']).install()


package(
    name='node',
    version='9.20171122',
    homepage='http://nodejs.org/',
    lib_depends={
        'c-ares',
        'cxx-runtime',
        'http-parser',
        'icu4c',
        'nghttp2',
        'zlib',
    },
    build_cmd=build)

distfile(
    name='node/f722d3122cd0c3d4a03bb2fb73998d6087e8318a.tar.gz',
    checksum='f9539ef716e44ba2a81f2420b8d0e50ee8b2e5e97bf7ac03275986413f880bf8',
    master_sites={'https://github.com/nodejs/node/archive/'},
    unsafe_string_sources={'deps/v8/src/base/file-utils.cc'})
