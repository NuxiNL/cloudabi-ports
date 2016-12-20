# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s')
    ctx.extract('cfe-%(version)s').rename(root.path('tools/clang'))
    ctx.extract('lld-%(version)s').rename(root.path('tools/lld'))

    # Build and install LLVM, Clang and LLD.
    build = root.cmake(['-DLLVM_TARGETS_TO_BUILD=AArch64;ARM;X86'])
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
    version='0.288619',
    homepage='http://llvm.org/',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-0.288619.tar.xz',
    checksum='10f4f149f1e5c2a170b7a2e8e84bec29c154deebc6d411513c621be92f2d0977',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
)
distfile(
    name='lld-0.288619.tar.xz',
    checksum='2681d75c62ce41313cd25bd8934637ca42e7b474bd0d4852ad8c957a7d4d3c70',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
)
distfile(
    name='llvm-0.288619.tar.xz',
    checksum='83a85fca8215973f6341f4c46aeb7736b2f604b57e292618d1fdf88dc7c0ae2e',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
)
