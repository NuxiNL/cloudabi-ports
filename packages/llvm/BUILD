# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    ctx.extract('cfe-%(version)s.src').rename(root.path('tools/clang'))
    ctx.extract('lld-%(version)s.src').rename(root.path('tools/lld'))

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
    version='3.8.0',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_depends={'cmake', 'ninja'},
    build_cmd=build,
)

distfile(
    name='cfe-3.8.0.src.tar.xz',
    checksum='04149236de03cf05232d68eb7cb9c50f03062e339b68f4f8a03b650a11536cf9',
    master_sites={'http://llvm.org/releases/3.8.0/'},
    patches={'safestack'},
)
distfile(
    name='lld-3.8.0.src.tar.xz',
    checksum='94704dda228c9f75f4403051085001440b458501ec97192eee06e8e67f7f9f0c',
    master_sites={'http://llvm.org/releases/3.8.0/'},
    patches={'start-stop-gc-sections'},
)
distfile(
    name='llvm-3.8.0.src.tar.xz',
    checksum='555b028e9ee0f6445ff8f949ea10e9cd8be0d084840e21fbbe1d31d51fc06e46',
    master_sites={'http://llvm.org/releases/3.8.0/'},
    patches={},
)
