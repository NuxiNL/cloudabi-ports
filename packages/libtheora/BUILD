def libtheora_build(ctx):
    root = ctx.distfile()
    build = root.autoconf(['--disable-examples'])
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='libtheora',
    version='1.1.1',
    homepage='http://www.theora.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libogg'},
    build_cmd=libtheora_build,
)

distfile(
    name='libtheora-1.1.1.tar.bz2',
    checksum='b6ae1ee2fa3d42ac489287d3ec34c5885730b1296f0801ae577a35193d3affbc',
    master_sites={'http://downloads.xiph.org/releases/theora/'},
)
