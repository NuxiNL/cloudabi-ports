def yaml_build(ctx):
  ctx.insert_sources(0, '.')
  ctx.run_autoconf()
  ctx.run_make(['noinst_PROGRAMS='])
  ctx.run_make_install(['noinst_PROGRAMS=', 'install'])

package(
    name = 'yaml',
    version = '0.1.6',
    homepage = 'http://pyyaml.org/wiki/LibYAML',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c-runtime'},
    build_cmd = yaml_build,
)

distfile(
    name = 'yaml-0.1.6.tar.gz',
    checksum = '7da6971b4bd08a986dd2a61353bc422362bd0edcc67d7ebaac68c95f74182749',
    master_sites = {'http://pyyaml.org/download/libyaml/'},
    patches = {'yaml/patch-no-sprintf'},
)
