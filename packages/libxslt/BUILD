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
    version='1.1.29',
    homepage='http://xmlsoft.org/libxslt/',
    lib_depends={'c-runtime', 'libxml2'},
    build_cmd=build)

distfile(
    name='libxslt-1.1.29.tar.gz',
    checksum='b5976e3857837e7617b29f2249ebb5eeac34e249208d31f1fbf7a6ba7a4090ce',
    master_sites={'http://xmlsoft.org/sources/'},
    unsafe_string_sources={
        'libxslt/functions.c',
        'libxslt/xsltutils.c',
    })
