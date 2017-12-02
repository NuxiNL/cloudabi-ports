# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


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
    version='1.1.32',
    homepage='http://xmlsoft.org/libxslt/',
    lib_depends={'c-runtime', 'libxml2'},
    build_cmd=build)

distfile(
    name='libxslt-1.1.32.tar.gz',
    checksum='526ecd0abaf4a7789041622c3950c0e7f2c4c8835471515fd77eec684a355460',
    master_sites={'http://xmlsoft.org/sources/'},
    unsafe_string_sources={
        'libxslt/functions.c',
        'libxslt/xsltutils.c',
    })
