# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('db-%(version)s').path('dist').gnu_configure([
        '--disable-mutexsupport',
        '--disable-replication',
        '--enable-cxx',
        'ac_cv_func_getcwd=yes',
        'ac_cv_func_printf=yes',
    ])
    build.make(['UTIL_PROGS='])
    build.make_install([
        'UTIL_PROGS=',
        'install_include',
        'install_lib',
    ]).install()


package(
    name='db48',
    version='4.8.30',
    homepage=
    'http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='db-4.8.30.tar.gz',
    checksum='e0491a07cdb21fb9aa82773bbbedaeb7639cbd0e7f96147ab46141e0045db72a',
    master_sites={'http://download.oracle.com/berkeley-db/'},
    unsafe_string_sources={
        'cxx/cxx_except.cpp',
        'db/partition.c',
        'dbm/dbm.c',
        'log/log_put.c',
        'os/os_getenv.c',
        'qam/qam_files.c',
    })
