# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-3.9.0rc1.src')
    ctx.extract('cfe-3.9.0rc1.src').rename(root.path('tools/clang'))
    ctx.extract('lld-3.9.0rc1.src').rename(root.path('tools/lld'))

    # Build and install LLVM, Clang and LLD.
    build = root.cmake(['-DLLVM_TARGETS_TO_BUILD=AArch64;X86'])
    build.ninja()
    stage = build.ninja_install()

    # Create symbolic links for various utilities, so that they can act
    # as cross build tools.
    bindir = stage.path('bin')
    for arch in ARCHITECTURES:
        bindir.path(arch + '-ar').symlink('llvm-ar')
        bindir.path(arch + '-c++').symlink('clang++')
        bindir.path(arch + '-cc').symlink('clang')
        bindir.path(arch + '-ld').symlink('lld')
        bindir.path(arch + '-nm').symlink('llvm-nm')
        bindir.path(arch + '-objdump').symlink('llvm-objdump')
        bindir.path(arch + '-ranlib').symlink('llvm-ranlib')

    # Only install the parts of LLVM that we actually use.
    bindir.install('bin')
    stage.path('lib/clang').install('lib/clang')

host_package(
    name='llvm',
    version='3.8.91',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-3.9.0rc1.src.tar.xz',
    checksum='56adfce2c14e0b90fade6ce4349e90120f12ea650832e80b95f4cb3b59510a1d',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc1/'},
    patches={
        'i686-no-pie',
        'omit-frame-pointer',
    },
)
distfile(
    name='lld-3.9.0rc1.src.tar.xz',
    checksum='d6d3dea1455ead52c17766d8560af11f3b9a712258f0a4eb7f3aaa9629225ff5',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc1/'},
    patches=set(),
)
distfile(
    name='llvm-3.9.0rc1.src.tar.xz',
    checksum='2b11e3e2221dc2844d341597abff9d1218caf9649f0e7cc87a1d6f1f92b9aa35',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc1/'},
    patches={
        'bug-28617',
        'bug-28863',
    },
)
