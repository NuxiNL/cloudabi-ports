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
    version='0.269026',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-0.269026.tar.xz',
    checksum='95cfed38bfb950c41da8fe34983065e384703ea85350a1047141920dd4da9060',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches={
        'i686-no-pie',
        'omit-frame-pointer',
    },
)
distfile(
    name='lld-0.269026.tar.xz',
    checksum='9d1abbfadd967a52d43a3976fece2055ed34fe814d8a3e5a1d7af9aef14a48d6',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches=set(),
)
distfile(
    name='llvm-0.269026.tar.xz',
    checksum='7dfa48b8f8ab4d3e4c3eeb026cc4e0447950ba958fedc725bba8a9d8718a1b06',
    master_sites={'https://nuxi.nl/distfiles/third_party/'},
    patches=set(),
)
