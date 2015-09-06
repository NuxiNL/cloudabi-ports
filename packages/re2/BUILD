def re2_build(ctx):
    root = ctx.extract('%(name)s/2015-08-01')
    root.make()
    root.make_install(['prefix=' + ctx.prefix(), 'install']).install()

package(
    name='re2',
    version='0.20150801',
    homepage='https://github.com/google/re2',
    maintainer='info@nuxi.nl',
    lib_depends={'c++-runtime'},
    build_cmd=re2_build,
)

distfile(
    name='re2/2015-08-01.tar.gz',
    checksum='0fd7388097dcc7b26a8fc7c4e704e2831d264015818fa3f13665f36d40afabf8',
    master_sites={'https://github.com/google/re2/archive/'},
    patches={
        're2/patch-makefile',
        're2/patch-snprintf'},
)
