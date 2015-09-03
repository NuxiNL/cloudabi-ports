def taglib_build(ctx):
  ctx.insert_sources()
  ctx.run_cmake(['-DENABLE_STATIC=ON'])
  ctx.run_make()
  ctx.run_make_install()

package(
    name = 'taglib',
    version = '1.9.1',
    homepage = 'https://taglib.github.io/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c++-runtime', 'zlib'},
    build_cmd = taglib_build,
)

distfile(
    name = 'taglib-1.9.1.tar.gz',
    checksum = '72d371cd1419a87ae200447a53bff2be219283071e80fd12337928cc967dc71a',
    master_sites = {'https://taglib.github.io/releases/'},
    patches = {'taglib/patch-no-fopen'},
)
