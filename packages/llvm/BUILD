# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    ctx.extract('cfe-%(version)s.src').rename(root.path('tools/clang'))
    ctx.extract('lld-%(version)s.src').rename(root.path('tools/lld'))

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
    version='3.9.0',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-3.9.0.src.tar.xz',
    checksum='7596a7c7d9376d0c89e60028fe1ceb4d3e535e8ea8b89e0eb094e0dcb3183d28',
    master_sites={'http://llvm.org/releases/3.9.0/'},
    patches={'arm'},
)
distfile(
    name='lld-3.9.0.src.tar.xz',
    checksum='986e8150ec5f457469a20666628bf634a5ca992a53e157f3b69dbc35056b32d9',
    master_sites={'http://llvm.org/releases/3.9.0/'},
    patches={
        'bug-30218',
        'r276095-r277369',
    },
)
distfile(
    name='llvm-3.9.0.src.tar.xz',
    checksum='66c73179da42cee1386371641241f79ded250e117a79f571bbd69e56daa48948',
    master_sites={'http://llvm.org/releases/3.9.0/'},
    patches=set(),
)
