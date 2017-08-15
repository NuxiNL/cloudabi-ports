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
    version='5.0.0',
    homepage='http://llvm.org/',
    build_depends={'cmake', 'ninja'},
    build_cmd=build)

distfile(
    name='cfe-5.0.0rc2.src.tar.xz',
    checksum='879548d82be18fa74658005bc1740c47e4432d767b79beb4d3aa2f27c0584eaa',
    master_sites={'http://prereleases.llvm.org/5.0.0/rc2/'},
    patches={'clang-no-c-headers'})
distfile(
    name='lld-5.0.0rc2.src.tar.xz',
    checksum='e112d06e8251339d54f9fd85a622c06b1f011847f9fc0547393d5f20f5fd8527',
    master_sites={'http://prereleases.llvm.org/5.0.0/rc2/'},
    patches=set())
distfile(
    name='llvm-5.0.0rc2.src.tar.xz',
    checksum='14442c8f5583c0aa5dcf73809828f9be57fedeb2191b00a8bd706a2954d19468',
    master_sites={'http://prereleases.llvm.org/5.0.0/rc2/'},
    patches=set())
