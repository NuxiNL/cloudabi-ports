def expat_build(ctx):
    ctx.distfile().autoconf().make_install(['installlib']).install()

package(
    name='expat',
    version='2.1.0',
    homepage='http://expat.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=expat_build,
)

distfile(
    name='expat-2.1.0.tar.gz',
    checksum='823705472f816df21c8f6aa026dd162b280806838bb55b3432b0fb1fcca7eb86',
    master_sites=sourceforge_sites('expat/expat/2.1.0'),
    patches={'expat/patch-no-srand'},
)
