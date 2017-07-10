# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


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
    version='8.40',
    homepage='http://www.pcre.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='pcre-8.40.tar.bz2',
    checksum='00e27a29ead4267e3de8111fcaa59b132d0533cdfdbdddf4b0604279acbcf4f4',
    master_sites={'ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/'},
    unsafe_string_sources={'pcreposix.c'})
