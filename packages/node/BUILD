# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/9f3d59eabb6564ad337a762d61ac767f9130e8a5')
    srcdir.run([
        'python2',
        './configure',
        '--dest-os=cloudabi',
        '--shared-cares',
        '--shared-http-parser',
        '--shared-libuv',
        '--shared-zlib',
        '--with-intl=system-icu',
        '--without-inspector',
        '--without-snapshot',
        '--without-ssl',
    ])
    srcdir.make()
    srcdir.make_install(['PREFIX=' + ctx.prefix(), 'install']).install()


package(
    name='node',
    version='9.20171105',
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
    name='node/9f3d59eabb6564ad337a762d61ac767f9130e8a5.tar.gz',
    checksum='23eada3a34fd52af435c23d6c8db9e014eb034bfdda9fb9f3d208465c31047c0',
    master_sites={'https://github.com/nodejs/node/archive/'},
    unsafe_string_sources={'deps/v8/src/base/file-utils.cc'})
