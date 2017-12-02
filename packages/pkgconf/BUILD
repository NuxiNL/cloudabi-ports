# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import os


def build(ctx):
    # Install a copy of pkgconf for every architecture under the name
    # <arch>-pkg-config. Each copy will use its own library and include
    # directory. Autoconf is smart enough to automatically detect the
    # right copy, based on the host type.
    for arch in ARCHITECTURES:
        prefix = ctx.prefix()
        arch_prefix = os.path.join(prefix, arch)
        srcdir = ctx.extract()
        srcdir.run(['./autogen.sh'])
        build = srcdir.gnu_configure([
            '--prefix=%s/pkgconf/%s' % (prefix, arch),
            '--with-pkg-config-dir=' +
            os.path.join(arch_prefix, 'lib/pkgconfig'),
            '--with-system-libdir=' + os.path.join(arch_prefix, 'lib'),
            '--with-system-includedir=' + os.path.join(arch_prefix, 'include'),
        ])
        build.make()
        stage = build.make_install()
        stage.path('bin/%s-pkg-config' % arch).symlink(
            '../pkgconf/%s/bin/pkgconf' % arch)
        stage.install()

    # Install the shipped copy of pkg.m4, so that autoreconf for
    # packages using PKG_CHECK_MODULES() works.
    ctx.extract().path('pkg.m4').install('share/aclocal/pkg.m4')


host_package(
    name='pkgconf',
    version='1.3.10',
    homepage='https://github.com/pkgconf/pkgconf',
    build_depends={'autoconf', 'automake', 'libtool', 'm4'},
    build_cmd=build)

distfile(
    name='pkgconf-1.3.10.tar.gz',
    checksum='b5d3e81297ebb0e00e0cb1d74583531cf0b20ada37e58193a55cac07e5a92b93',
    master_sites={'https://github.com/pkgconf/pkgconf/archive/'})
