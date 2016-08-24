# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-3.9.0rc2.src')
    ctx.extract('cfe-3.9.0rc2.src').rename(root.path('tools/clang'))
    ctx.extract('lld-3.9.0rc2.src').rename(root.path('tools/lld'))

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
    version='3.8.92',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-3.9.0rc2.src.tar.xz',
    checksum='2d2d7aad5c7b67dd2bd324d0ce10435a797a85b04fa06e4944a6143dfefb4b89',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc2/'},
    patches=set(),
)
distfile(
    name='lld-3.9.0rc2.src.tar.xz',
    checksum='4524ada47c4d392cda9f3de3e7132aac9d704bc3ef613d5589059a1563b47c1e',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc2/'},
    patches={'bug-29068'},
)
distfile(
    name='llvm-3.9.0rc2.src.tar.xz',
    checksum='d7516c9887f6a6ba0ac40fa394f0fd09a65e0b5721468fc85db8a13b47d1dc69',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc2/'},
    patches=set(),
)
