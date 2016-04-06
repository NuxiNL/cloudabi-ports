# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s')
    ctx.extract('cfe-%(version)s').rename(root.path('tools/clang'))
    ctx.extract('lld-%(version)s').rename(root.path('tools/lld'))

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
    version='0.265546',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-0.265546.tar.xz',
    checksum='56f757dcdd54348984743e95f06ece9aab1d555f7b8a2c2a735974e3f0818ea4',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches=set(),
)
distfile(
    name='lld-0.265546.tar.xz',
    checksum='9caecac4bd850fe1ff4dd4d9c8642a6822a11e50c07e3f5ebb3d793ce2bd4bf4',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches={'relocations'},
)
distfile(
    name='llvm-0.265546.tar.xz',
    checksum='74d532de88aae504933de7d9ffa5d1510c64956a9e9a9ebef74f444567a6f42f',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches=set(),
)
