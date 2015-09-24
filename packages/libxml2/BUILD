# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf([
        '--without-ftp', '--without-http', '--without-python',
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
    version='2.9.2',
    homepage='http://www.xmlsoft.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libxml2-2.9.2.tar.gz',
    checksum='5178c30b151d044aefb1b08bf54c3003a0ac55c59c866763997529d60770d5bc',
    master_sites={'ftp://xmlsoft.org/libxml2/'},
)
