# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['buildlib'])
    build.make_install(['installlib']).install()

package(
    name='expat',
    version='2.1.1',
    homepage='http://expat.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='expat-2.1.1.tar.bz2',
    checksum='aff584e5a2f759dcfc6d48671e9529f6afe1e30b0cd6a4cec200cbe3f793de67',
    master_sites=sites_sourceforge('expat/expat/2.1.1'),
)
