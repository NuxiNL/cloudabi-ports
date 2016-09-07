# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    build = srcdir.gnu_configure([
        '--disable-pcre2grep-callout', '--enable-jit',
        '--enable-pcre2-16', '--enable-pcre2-32',
    ])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    stage = build.make_install([
        'bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install',
    ])
    stage.path('bin/pcre2-config').unhardcode_paths()
    stage.install()

package(
    name='pcre2',
    version='10.22',
    homepage='http://www.pcre.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='pcre2-10.22.tar.bz2',
    checksum='b2b44619f4ac6c50ad74c2865fd56807571392496fae1c9ad7a70993d018f416',
    master_sites={'ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/'},
    unsafe_string_sources={
        'src/pcre2_error.c',
        'src/pcre2posix.c',
    },
)
