# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure([
        '--without-debug', '--without-ftp',
        '--without-http', '--without-python',
    ])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'noinst_LTLIBRARIES='])
    stage = build.make_install([
        'bin_PROGRAMS=', 'noinst_PROGRAMS=', 'noinst_LTLIBRARIES=', 'install',
    ])
    stage.path('bin/xml2-config').unhardcode_paths()
    stage.path('lib/xml2Conf.sh').unhardcode_paths()
    stage.install()

package(
    name='libxml2',
    version='2.9.4',
    homepage='http://www.xmlsoft.org/',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libxml2-2.9.4.tar.gz',
    checksum='ffb911191e509b966deb55de705387f14156e1a56b21824357cdf0053233633c',
    master_sites={'ftp://xmlsoft.org/libxml2/'},
    unsafe_string_sources={
        'HTMLparser.c',
        'valid.c',
        'xmlmemory.c',
    },
)
