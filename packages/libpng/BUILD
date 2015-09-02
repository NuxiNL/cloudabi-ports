def libpng_build(ctx):
  ctx.insert_sources(0, '.')
  ctx.run_autoconf()
  ctx.run_make(['bin_PROGRAMS=', 'check_PROGRAMS='])
  ctx.run_make_install(['bin_PROGRAMS=', 'check_PROGRAMS=', 'install'])

package(
    name = 'libpng',
    version = '1.6.18',
    homepage = 'http://www.libpng.org/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c-runtime', 'zlib'},
    build_cmd = libpng_build,
)

distfile(
    name = 'libpng-1.6.18.tar.xz',
    checksum = '2e10c13b7949883ac961db6177c516d778184432d440317e9f0391305c360963',
    master_sites = sourceforge_sites('libpng/libpng16/1.6.18'),
    patches = {'libpng/patch-no-fopen', 'libpng/patch-no-gmtime'},
)
