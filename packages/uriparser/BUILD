def uriparser_build(ctx):
    build = ctx.extract().autoconf(['--disable-doc', '--disable-test'])
    build.make(['bin_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'install']).install()

package(
    name='uriparser',
    version='0.8.2',
    homepage='http://uriparser.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=uriparser_build,
)

distfile(
    name='uriparser-0.8.2.tar.bz2',
    checksum='6d6e66b0615f65e9e2391933dab7e45eca0947160f10c6b47bc50feda93e508f',
    master_sites=sourceforge_sites('uriparser/Sources/0.8.2'),
)
