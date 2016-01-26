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
    version='2.26',
    homepage='https://www.gnu.org/software/binutils/',
    maintainer='info@nuxi.nl',
    build_depends={'bison', 'flex', 'make'},
    build_cmd=build,
)

distfile(
    name='binutils-2.26.tar.bz2',
    checksum='c2ace41809542f5237afc7e3b8f32bb92bc7bc53c6232a84463c423b0714ecd9',
    master_sites=sites_gnu('binutils'),
)
