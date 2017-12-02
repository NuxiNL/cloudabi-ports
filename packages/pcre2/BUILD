# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract()
    build = srcdir.gnu_configure([
        '--disable-pcre2grep-callout',
        '--enable-jit',
        '--enable-pcre2-16',
        '--enable-pcre2-32',
    ])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    stage = build.make_install([
        'bin_PROGRAMS=',
        'noinst_PROGRAMS=',
        'install',
    ])
    stage.path('bin/pcre2-config').unhardcode_paths()
    stage.install()


package(
    name='pcre2',
    version='10.30',
    homepage='http://www.pcre.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='pcre2-10.30.tar.bz2',
    checksum='90bd41c605d30e3745771eb81928d779f158081a51b2f314bbcc1f73de5773db',
    master_sites={'ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/'},
    unsafe_string_sources={
        'src/pcre2_error.c',
        'src/pcre2posix.c',
    })
