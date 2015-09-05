def libxspf_build(ctx):
    ctx.distfile().autoconf(['--disable-test']).make_install([
        'bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install',
    ]).install()

package(
    name='libxspf',
    version='1.2.0',
    homepage='http://libspiff.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c++-runtime', 'expat', 'uriparser'},
    build_cmd=libxspf_build,
)

distfile(
    name='libxspf-1.2.0.tar.bz2',
    checksum='ba9e93a0066469b074b4022b480004651ad3aa5b4313187fd407d833f79b43a5',
    master_sites=sourceforge_sites('libspiff/Sources/1.2.0'),
    patches={
        'libxspf/patch-no-fopen',
        'libxspf/patch-no-strcpy'},
)
