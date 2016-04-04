# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s')
    ctx.extract('cfe-%(version)s').rename(root.path('tools/clang'))
    ctx.extract('lld-%(version)s').rename(root.path('tools/lld'))

    # Build and install LLVM, Clang and LLD.
    build = root.cmake()
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
    version='0.265258',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-0.265258.tar.xz',
    checksum='19a036e7404aafce7d6ac1de68032f308c6af323149df330da74257744660c21',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches={'force-pie'},
)
distfile(
    name='lld-0.265258.tar.xz',
    checksum='9f2f3a1df110762689e32bd09453791110f230bee794fb43ac6d873b8ce2ee0f',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches={'relocations'},
)
distfile(
    name='llvm-0.265258.tar.xz',
    checksum='9c528d30027eed5b48cb112e8a5985a7de32f8f5963ebefa90673d852c3c32cd',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches=set(),
)
