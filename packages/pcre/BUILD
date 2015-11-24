# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract()
    build = srcdir.autoconf([
        '--enable-jit', '--enable-pcre16', '--enable-pcre32',
    ])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    stage = build.make_install([
        'bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install',
    ])
    stage.path('bin/pcre-config').unhardcode_paths()
    stage.install()

package(
    name='pcre',
    version='8.38',
    homepage='http://www.pcre.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='pcre-8.38.tar.bz2',
    checksum='b9e02d36e23024d6c02a2e5b25204b3a4fa6ade43e0a5f869f254f49535079df',
    master_sites={'ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/'},
    unsafe_string_sources={'pcreposix.c'},
)
