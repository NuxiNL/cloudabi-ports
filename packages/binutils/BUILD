def build(ctx):
    root = ctx.extract()
    for arch in ARCHITECTURES:
        build = root.autoconf([
            '--target=' + arch,
            '--disable-gdb',
            '--disable-nls',
            '--disable-werror',
            '--enable-deterministic-archives'])
        build.make()
        stage = build.make_install()

        # Remove extraneous '<arch>/bin' directory. We shouldn't keep
        # binaries from the host system in this directory.
        stage.path(arch).path('bin').remove()
        stage.path('share/info').remove()
        stage.install()

host_package(
    name='binutils',
    version='2.25.1',
    homepage='http://www.gnu.org/software/binutils/',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='binutils-2.25.1.tar.bz2',
    checksum='b5b14added7d78a8d1ca70b5cb75fef57ce2197264f4f5835326b0df22ac9f22',
    master_sites={'http://ftp.gnu.org/gnu/binutils/'},
    patches={'cloudabi'},
)
