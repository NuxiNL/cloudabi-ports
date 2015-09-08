def build(ctx):
    build = ctx.extract().autoconf(['--without-iconv'])
    build.make()
    build.make_install().install()

host_package(
    name='libarchive',
    version='3.1.2',
    homepage='http://www.libarchive.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'xz'},
    build_cmd=build,
)

distfile(
    name='libarchive-3.1.2.tar.gz',
    checksum='eb87eacd8fe49e8d90c8fdc189813023ccc319c5e752b01fb6ad0cc7b2c53d5e',
    master_sites={'http://www.libarchive.org/downloads/'},
    patches={'no-metadata'},
)
