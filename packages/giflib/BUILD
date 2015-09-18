# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install([
        'bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install',
    ]).install()

package(
    name='giflib',
    version='5.1.1',
    homepage='http://giflib.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='giflib-5.1.1.tar.bz2',
    checksum='391014aceb21c8b489dc7b0d0b6a917c4e32cc014ce2426d47ca376d02fe2ffc',
    master_sites=sites_sourceforge('giflib'),
    patches={
        'no-fopen',
        'no-strcpy',
        'no-strtok',
    },
)
