def zlib_build(root):
  root.insert_sources()
  root.run(['./configure'])
  root.make(['libz.a'])

  root.path('libz.a').install('lib/libz.a')
  root.path('zconf.h').install('include/zconf.h')
  root.path('zlib.h').install('include/zlib.h')

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
