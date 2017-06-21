# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    ctx.extract('cfe-%(version)s.src').rename(root.path('tools/clang'))
    ctx.extract('lld-%(version)s.src').rename(root.path('tools/lld'))

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
    name='cfe-4.0.0.src.tar.xz',
    checksum='cea5f88ebddb30e296ca89130c83b9d46c2d833685e2912303c828054c4dc98a',
    master_sites={'http://www.llvm.org/releases/4.0.0/'},
    patches={'clang-no-c-headers'},
)
distfile(
    name='lld-4.0.0.src.tar.xz',
    checksum='33e06457b9ce0563c89b11ccc7ccabf9cff71b83571985a5bf8684c9150e7502',
    master_sites={'http://www.llvm.org/releases/4.0.0/'},
    patches={'r295240'},
)
distfile(
    name='llvm-4.0.0.src.tar.xz',
    checksum='8d10511df96e73b8ff9e7abbfb4d4d432edbdbe965f1f4f07afaf370b8a533be',
    master_sites={'http://www.llvm.org/releases/4.0.0/'},
    patches=set(),
)
