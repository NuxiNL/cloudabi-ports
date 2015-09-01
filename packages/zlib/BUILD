def zlib_build(ctx):
  ctx.insert_sources(0, '.')
  ctx.run_command('.', ['./configure'])
  ctx.run_command('.', ['make', 'libz.a'])

  ctx.install('libz.a', 'lib/libz.a')
  ctx.install('zconf.h', 'include/zconf.h')
  ctx.install('zlib.h', 'include/zlib.h')

package(
    name = 'zlib',
    version = '1.2.8',
    homepage = 'http://www.zlib.net/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c-runtime'},
    build_cmd = zlib_build,
)

distfile(
    name = 'zlib-1.2.8.tar.xz',
    checksum = '831df043236df8e9a7667b9e3bb37e1fcb1220a0f163b6de2626774b9590d057',
    master_sites = {'http://zlib.net/'},
    patches = {'zlib/patch-no-gzopen'},
)
