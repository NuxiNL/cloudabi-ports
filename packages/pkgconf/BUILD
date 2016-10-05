# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

import os


def build(ctx):
    # Install a copy of pkgconf for every architecture under the name
    # <arch>-pkg-config. Each copy will use its own library and include
    # directory. Autoconf is smart enough to automatically detect the
    # right copy, based on the host type.
    for arch in ARCHITECTURES:
        prefix = os.path.join(ctx.prefix(), arch)
        build = ctx.extract().gnu_configure([
            '--with-pkg-config-dir=' + os.path.join(prefix, 'lib/pkgconfig'),
            '--with-system-libdir=' + os.path.join(prefix, 'lib'),
            '--with-system-includedir=' + os.path.join(prefix, 'include'),
        ], inplace=True)
        build.make()
        stage = build.make_install()
        stage.path('bin/pkgconf').install('bin/%s-pkg-config' % arch)

    # Install the shipped copy of pkg.m4, so that autoreconf for
    # packages using PKG_CHECK_MODULES() works.
    ctx.extract().path('pkg.m4').install('share/aclocal/pkg.m4')

host_package(
    name='pkgconf',
    version='0.9.12',
    homepage='https://github.com/pkgconf/pkgconf',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='pkgconf-0.9.12.tar.bz2',
    checksum='7ec8b516e655e247f4ba976837cee808134785819ab8f538f652fe919cc6c09f',
    master_sites={'http://rabbit.dereferenced.org/~nenolod/distfiles/'},
)
