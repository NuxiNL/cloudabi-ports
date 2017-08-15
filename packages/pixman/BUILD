# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure(
        ['--disable-arm-neon', '--disable-arm-simd'])
    build.make(['noinst_LTLIBRARIES=', 'noinst_PROGRAMS='])
    build.make_install([
        'noinst_LTLIBRARIES=',
        'noinst_PROGRAMS=',
        'install',
    ]).install()


package(
    name='pixman',
    version='0.34.0',
    homepage='http://www.pixman.org/',
    lib_depends={'c-runtime'},
    build_cmd=build)

distfile(
    name='pixman-0.34.0.tar.gz',
    checksum='21b6b249b51c6800dc9553b65106e1e37d0e25df942c90531d4c3997aa20a88e',
    master_sites={'http://cairographics.org/releases/'})
