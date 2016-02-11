# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-3.8.0rc2.src')
    ctx.extract('cfe-3.8.0rc2.src').rename(root.path('tools/clang'))
    ctx.extract('lld-3.8.0rc2.src').rename(root.path('tools/lld'))

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
    version='3.7.92',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-3.8.0rc2.src.tar.xz',
    checksum='94b0e158a31573c4bb47b872fea08c49f4e6754a4de2bacdc20db231c9ace9b6',
    master_sites={'http://llvm.org/pre-releases/3.8.0/rc2/'},
)
distfile(
    name='lld-3.8.0rc2.src.tar.xz',
    checksum='03c328d2d126b65dae2619b9195a4177818c8451d5b843bbc4110c300bcd1a23',
    master_sites={'http://llvm.org/pre-releases/3.8.0/rc2/'},
)
distfile(
    name='llvm-3.8.0rc2.src.tar.xz',
    checksum='8141ba68fde29e213fb82886b58b722d9c2aa2179116d1e7f8a7d6de23508047',
    master_sites={'http://llvm.org/pre-releases/3.8.0/rc2/'},
)
