# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['buildlib'])
    build.make_install(['installlib']).install()

package(
    name='expat',
    version='2.1.0',
    homepage='http://expat.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='expat-2.1.0.tar.gz',
    checksum='823705472f816df21c8f6aa026dd162b280806838bb55b3432b0fb1fcca7eb86',
    master_sites=sites_sourceforge('expat/expat/2.1.0'),
)
