# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    for arch in ARCHITECTURES:
        build = root.autoconf([
            '--target=' + arch,
            '--disable-gdb',
            '--disable-nls',
            '--disable-werror',
        ])
        build.make()

        # Only install the linker and strip.
        stage = build.make_install()
        for bin in {'ld', 'strip'}:
            filename = 'bin/%s-%s' % (arch, bin)
            stage.path(filename).install(filename)
        filename = '%s/lib/ldscripts' % arch
        stage.path(filename).install(filename)

host_package(
    name='binutils',
    version='2.26.51',
    homepage='https://www.gnu.org/software/binutils/',
    maintainer='info@nuxi.nl',
    build_depends={'bison', 'flex', 'make'},
    build_cmd=build,
)

distfile(
    name='binutils-2.26.51.tar.bz2',
    checksum='b1c55ea8dd7d70ab8b5a03bbeb86cbbef0f9dd18aa7be085141666e5096992ac',
    master_sites={'ftp://sourceware.org/pub/binutils/snapshots/'},
)
