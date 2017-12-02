# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure([
        '--without-debug',
        '--without-ftp',
        '--without-http',
        '--without-python',
    ])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'noinst_LTLIBRARIES='])
    stage = build.make_install([
        'bin_PROGRAMS=',
        'noinst_PROGRAMS=',
        'noinst_LTLIBRARIES=',
        'install',
    ])
    stage.path('bin/xml2-config').unhardcode_paths()
    stage.path('lib/xml2Conf.sh').unhardcode_paths()
    stage.install()


package(
    name='libxml2',
    version='2.9.7',
    homepage='http://www.xmlsoft.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='libxml2-2.9.7.tar.gz',
    checksum='f63c5e7d30362ed28b38bfa1ac6313f9a80230720b7fb6c80575eeab3ff5900c',
    master_sites={'ftp://xmlsoft.org/libxml2/'},
    unsafe_string_sources={
        'HTMLparser.c',
        'valid.c',
        'xmlmemory.c',
    })
