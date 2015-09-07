def build(ctx):
    build = ctx.extract().autoconf([
        '--disable-lzmadec', '--disable-lzmainfo', '--disable-scripts',
        '--disable-xz', '--disable-xzdec',
    ])
    build.make()
    build.make_install().install()

package(
    name='xz',
    version='5.2.1',
    homepage='http://tukaani.org/xz/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='xz-5.2.1.tar.xz',
    checksum='6ecdd4d80b12001497df0741d6037f918d270fa0f9a1ab4e2664bf4157ae323c',
    master_sites={'http://tukaani.org/xz/'},
    patches={'no-signals'},
)
