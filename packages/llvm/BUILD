def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    ctx.extract('cfe-%(version)s.src').rename(root.path('tools/clang'))

    # Build and install LLVM.
    build = root.cmake()
    build.make()
    stage = build.make_install()

    # Create symbolic links for Clang, so that it can act as a cross compiler.
    bindir = stage.path('bin')
    for arch in ARCHITECTURES:
        bindir.path(arch + '-cc').symlink('clang')
        bindir.path(arch + '-c++').symlink('clang++')

    # Only install the parts of LLVM that we actually use.
    bindir.install('bin')
    stage.path('lib/clang').install('lib/clang')

host_package(
    name='llvm',
    version='3.7.0',
    homepage='http://llvm.org/',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='cfe-3.7.0.src.tar.xz',
    checksum='4ed740c5a91df1c90a4118c5154851d6a475f39a91346bdf268c1c29c13aa1cc',
    master_sites={'http://llvm.org/releases/3.7.0/'},
    patches={'implicit-library-functions'},
)
distfile(
    name='llvm-3.7.0.src.tar.xz',
    checksum='ab45895f9dcdad1e140a3a79fd709f64b05ad7364e308c0e582c5b02e9cc3153',
    master_sites={'http://llvm.org/releases/3.7.0/'},
)
