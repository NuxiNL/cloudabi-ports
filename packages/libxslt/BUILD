# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    build = srcdir.gnu_configure(['--with-libxml-prefix=' + ctx.localbase()])
    build.make(['bin_PROGRAMS='])
    stage = build.make_install(['bin_PROGRAMS=', 'install'])

    # Remove hardcoded paths from utilities and headers.
    stage.path('bin/xslt-config').unhardcode_paths()
    stage.path('include/libxslt/xsltconfig.h').unhardcode_paths()
    stage.path('lib/xsltConf.sh').unhardcode_paths()
    stage.install()

package(
    name='libxslt',
    version='1.1.28',
    homepage='http://xmlsoft.org/libxslt/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libxml2'},
    build_cmd=build,
)

distfile(
    name='libxslt-1.1.28.tar.gz',
    checksum='5fc7151a57b89c03d7b825df5a0fae0a8d5f05674c0e7cf2937ecec4d54a028c',
    master_sites={'http://xmlsoft.org/sources/'},
    unsafe_string_sources={
        'libxslt/functions.c',
        'libxslt/xsltutils.c',
    },
)
