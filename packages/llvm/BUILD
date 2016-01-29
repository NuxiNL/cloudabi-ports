# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-3.8.0rc1.src')
    ctx.extract('cfe-3.8.0rc1.src').rename(root.path('tools/clang'))
    ctx.extract('lld-3.8.0rc1.src').rename(root.path('tools/lld'))

    # Build and install LLVM, Clang and LLD.
    build = root.cmake()
    build.ninja()
    stage = build.ninja_install()

    # Create symbolic links for various LLVM and Clang utilities, so
    # that it can act as a cross compiler.
    bindir = stage.path('bin')
    for arch in ARCHITECTURES:
        bindir.path(arch + '-ar').symlink('llvm-ar')
        bindir.path(arch + '-c++').symlink('clang++')
        bindir.path(arch + '-cc').symlink('clang')
        bindir.path(arch + '-nm').symlink('llvm-nm')
        bindir.path(arch + '-objdump').symlink('llvm-objdump')
        bindir.path(arch + '-ranlib').symlink('llvm-ranlib')

    # Only install the parts of LLVM that we actually use.
    bindir.install('bin')
    stage.path('lib/clang').install('lib/clang')

    # Install ld, a tiny wrapper around LLD, invoking it in such a way
    # that it acts as the GNU linker. Don't use LLD on aarch64 yet, as
    # support for that platform is not yet complete.
    ld = ctx.executable({
        ctx.resource('ld.c').compile([
            '-DPATH_LLD="%s/bin/lld"' % ctx.prefix(),
        ]),
    })
    for arch in ARCHITECTURES:
        if not arch.startswith('aarch64-'):
            ld.install('bin/%s-ld' % arch)

host_package(
    name='llvm',
    version='3.7.91',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-3.8.0rc1.src.tar.xz',
    checksum='11cd5e001fe83a55040a976c8e7d7b2c808534980df16b97b200b3b897df89c3',
    master_sites={'http://llvm.org/pre-releases/3.8.0/rc1/'},
)
distfile(
    name='lld-3.8.0rc1.src.tar.xz',
    checksum='7cf97833bd471362255340125defe14dcc89678bb89a13e1a205bdda9c456e8e',
    master_sites={'http://llvm.org/pre-releases/3.8.0/rc1/'},
)
distfile(
    name='llvm-3.8.0rc1.src.tar.xz',
    checksum='41809e45cb3a97908c5741b4c15c90d801793e09d75858a6cfaa9582f233249b',
    master_sites={'http://llvm.org/pre-releases/3.8.0/rc1/'},
)
