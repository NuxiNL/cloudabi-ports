# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    for wrap in {
            'connect_wrap',
            'fs_event_wrap',
            'node_file',
            'node_os',
            'node_stat_watcher',
            'process_wrap',
            'signal_wrap',
            'spawn_sync',
            'tty_wrap',
            'udp_wrap',
    }:
        srcdir.path('src/%s.cc' % wrap).remove()
        srcdir.path('src/%s.h' % wrap).remove()
    srcdir.run([
        '/usr/local/bin/python2',
        'configure',
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
    version='8.8.1',
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
    name='node/v8.8.1.tar.gz',
    checksum='c32ffc0938abb19f034aabebd56557e005dbca7654d2ebd6c74c4b976f82a7a0',
    master_sites={'https://github.com/nodejs/node/archive/'},
    unsafe_string_sources={'deps/v8/src/base/file-utils.cc'})
