# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)src2.src')
    ctx.extract('cfe-%(version)src2.src').rename(root.path('tools/clang'))
    ctx.extract('lld-%(version)src2.src').rename(root.path('tools/lld'))

    # Build and install LLVM, Clang and LLD.
    build = root.cmake([
        '-DLLVM_ENABLE_OCAMLDOC=NO',
        '-DLLVM_TARGETS_TO_BUILD=AArch64;ARM;X86',
    ])
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
    version='4.0.0',
    homepage='http://llvm.org/',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-4.0.0rc2.src.tar.xz',
    checksum='76d6c9b7f388a93a0303dbbac0e42b183b242f822b65eb44064679e7c36aa5dc',
    master_sites={'http://www.llvm.org/pre-releases/4.0.0/rc2/'},
    patches=set(),
)
distfile(
    name='lld-4.0.0rc2.src.tar.xz',
    checksum='37381d14b13fee27bffef0b6d2650d82c79d69100385f6fa181a0034c2aa9b90',
    master_sites={'http://www.llvm.org/pre-releases/4.0.0/rc2/'},
    patches={'r295240'},
)
distfile(
    name='llvm-4.0.0rc2.src.tar.xz',
    checksum='2257faed3795fedfc509d6dd5905be158231c508c6fcaaa02e4a09c5e8dadbe1',
    master_sites={'http://www.llvm.org/pre-releases/4.0.0/rc2/'},
    patches=set(),
)
