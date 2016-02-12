# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install([
        'bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install',
    ]).install()

package(
    name='giflib',
    version='5.1.2',
    homepage='http://giflib.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='giflib-5.1.2.tar.bz2',
    checksum='76c0a084c3b02f9315ff937b8be6096186002fea26f33e2123081ba2be6e2a7c',
    master_sites=sites_sourceforge('giflib'),
    unsafe_string_sources={
        'lib/gif_font.c',
        'util/getarg.c',
    },
)
