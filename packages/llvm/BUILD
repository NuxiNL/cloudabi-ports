# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-3.9.0rc3.src')
    ctx.extract('cfe-3.9.0rc3.src').rename(root.path('tools/clang'))
    ctx.extract('lld-3.9.0rc3.src').rename(root.path('tools/lld'))

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
    version='3.8.93',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-3.9.0rc3.src.tar.xz',
    checksum='cb06bb2403cc13bd2bc561222a9854d1aa52d96cf48b4a24d9e4b0b6832c96ec',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc3/'},
    patches={'arm'},
)
distfile(
    name='lld-3.9.0rc3.src.tar.xz',
    checksum='9532dc6940516785a3186571378dc0d94484722cfc17396583dfbe16246c2494',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc3/'},
    patches={
        'bug-30218',
        'r276095',
    },
)
distfile(
    name='llvm-3.9.0rc3.src.tar.xz',
    checksum='b52ed8390a9b7c30ab88cd679f890b5cac17ec52f7fe10bfc305b4d7254e3f82',
    master_sites={'http://llvm.org/pre-releases/3.9.0/rc3/'},
    patches=set(),
)
