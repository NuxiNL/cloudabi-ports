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

        # We only need the readelf and strip utilities, except on
        # aarch64. On aarch64, we also install the linker, as LLD does
        # not yet support this architecture completely.
        stage = build.make_install()
        filenames = {'bin/%s-readelf' % arch, 'bin/%s-strip' % arch}
        # TODO(ed): Use GNU ld as long as LLVM bug 22906 is not fixed.
        # if arch.startswith('aarch64-'):
        #     filenames |= {'bin/%s-ld' % arch, '%s/lib/ldscripts' % arch}
        filenames |= {'bin/%s-ld' % arch, '%s/lib/ldscripts' % arch}
        for filename in filenames:
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
