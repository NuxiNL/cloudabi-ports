def libtheora_build(ctx):
  ctx.insert_sources(0, '.')
  ctx.run_autoconf(['--disable-examples'])
  ctx.run_make()
  ctx.run_make_install()

package(
    name = 'libtheora',
    version = '1.1.1',
    homepage = 'http://www.theora.org/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c-runtime', 'libogg'},
    build_cmd = libtheora_build,
)

distfile(
    name = 'libtheora-1.1.1.tar.bz2',
    checksum = 'b6ae1ee2fa3d42ac489287d3ec34c5885730b1296f0801ae577a35193d3affbc',
    master_sites = {'http://downloads.xiph.org/releases/theora/'},
)
