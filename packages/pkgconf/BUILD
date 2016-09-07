# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
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

host_package(
    name='pkgconf',
    version='1.0.1',
    homepage='https://github.com/pkgconf/pkgconf',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='pkgconf-1.0.1.tar.xz',
    checksum='37db912cf060ed0a3113114515597f3c566d3ab796973c5c408691e20ec1fe20',
    master_sites={'https://github.com/pkgconf/pkgconf/releases/download/pkgconf-1.0.1/'},
)
