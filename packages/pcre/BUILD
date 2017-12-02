# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract()
    build = srcdir.gnu_configure([
        '--enable-jit',
        '--enable-pcre16',
        '--enable-pcre32',
    ])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    stage = build.make_install([
        'bin_PROGRAMS=',
        'noinst_PROGRAMS=',
        'install',
    ])
    stage.path('bin/pcre-config').unhardcode_paths()
    stage.install()


package(
    name='pcre',
    version='8.41',
    homepage='http://www.pcre.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='pcre-8.41.tar.bz2',
    checksum='e62c7eac5ae7c0e7286db61ff82912e1c0b7a0c13706616e94a7dd729321b530',
    master_sites={'ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/'},
    unsafe_string_sources={'pcreposix.c'})
