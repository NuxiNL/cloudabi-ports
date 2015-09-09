# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.

import os


def build(ctx):
    # Install a copy of pkgconf for every architecture under the name
    # <arch>-pkg-config. Each copy will use its own library and include
    # directory. Autoconf is smart enough to automatically detect the
    # right copy, based on the host type.
    root = ctx.extract()
    for arch in ARCHITECTURES:
        prefix = os.path.join(ctx.prefix(), arch)
        build = root.autoconf([
            '--with-pkg-config-dir=' + os.path.join(prefix, 'lib/pkgconfig'),
            '--with-system-libdir=' + os.path.join(prefix, 'lib'),
            '--with-system-includedir=' + os.path.join(prefix, 'include'),
        ], inplace=True)
        build.make()
        stage = build.make_install()
        stage.path('bin/pkgconf').install('bin/%s-pkg-config' % arch)

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
