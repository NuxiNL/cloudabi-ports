# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    stage = build.make_install(
        ['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install'])
    stage.path('share/man/man1').remove()
    stage.install()

package(
    name='libtasn1',
    version='4.7',
    homepage='https://www.gnu.org/software/libtasn1/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='libtasn1-4.7.tar.gz',
    checksum='a40780dc93fc6d819170240e8ece25352058a85fd1d2347ce0f143667d8f11c9',
    master_sites={'http://ftp.gnu.org/gnu/libtasn1/'},
)
