# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


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
    version='5.0.0',
    homepage='http://llvm.org/',
    build_depends={'cmake', 'ninja'},
    build_cmd=build)

distfile(
    name='cfe-5.0.0.src.tar.xz',
    checksum='019f23c2192df793ac746595e94a403908749f8e0c484b403476d2611dd20970',
    master_sites={'http://releases.llvm.org/5.0.0/'},
    patches={'clang-no-c-headers'})
distfile(
    name='lld-5.0.0.src.tar.xz',
    checksum='399a7920a5278d42c46a7bf7e4191820ec2301457a7d0d4fcc9a4ac05dd53897',
    master_sites={'http://releases.llvm.org/5.0.0/'},
    patches=set())
distfile(
    name='llvm-5.0.0.src.tar.xz',
    checksum='e35dcbae6084adcf4abb32514127c5eabd7d63b733852ccdb31e06f1373136da',
    master_sites={'http://releases.llvm.org/5.0.0/'},
    patches={'r317358'})
