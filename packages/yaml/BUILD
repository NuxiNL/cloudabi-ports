def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='yaml',
    version='0.1.6',
    homepage='http://pyyaml.org/wiki/LibYAML',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='yaml-0.1.6.tar.gz',
    checksum='7da6971b4bd08a986dd2a61353bc422362bd0edcc67d7ebaac68c95f74182749',
    master_sites={'http://pyyaml.org/download/libyaml/'},
    patches={'no-sprintf'},
)
