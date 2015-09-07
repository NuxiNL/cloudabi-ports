def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['noinst_LTLIBRARIES=', 'noinst_PROGRAMS='])
    build.make_install([
        'noinst_LTLIBRARIES=', 'noinst_PROGRAMS=', 'install',
    ]).install()

package(
    name='pixman',
    version='0.32.6',
    homepage='http://www.pixman.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='pixman-0.32.6.tar.gz',
    checksum='3dfed13b8060eadabf0a4945c7045b7793cc7e3e910e748a8bb0f0dc3e794904',
    master_sites={'http://cairographics.org/releases/'},
    patches={
        'asm-constraints',
        'no-printf',
    },
)
