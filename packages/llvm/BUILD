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
    version='0.265577',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-0.265577.tar.xz',
    checksum='0fa3762ff2711e18678c3a0d163f48ca60328135030eebe39c4d34bbef73ea4e',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
)
distfile(
    name='lld-0.265577.tar.xz',
    checksum='c0a840c9079d71ccac7bee19d397f7454cb08e67fb832a7ffe667e84ddb7ec8e',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
)
distfile(
    name='llvm-0.265577.tar.xz',
    checksum='312d830291d61ab0224f390bde5292a527fa7ff3b5ea879b2fb7472c24e43bc3',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
)
