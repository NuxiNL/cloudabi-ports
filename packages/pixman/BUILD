# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['noinst_LTLIBRARIES=', 'noinst_PROGRAMS='])
    build.make_install([
        'noinst_LTLIBRARIES=', 'noinst_PROGRAMS=', 'install',
    ]).install()

package(
    name='pixman',
    version='0.32.8',
    homepage='http://www.pixman.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='pixman-0.32.8.tar.gz',
    checksum='575ade17c40b47d391b02b4c0c63531c897b31e70046c96749514b7d8800d65d',
    master_sites={'http://cairographics.org/releases/'},
)
