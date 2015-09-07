def build(ctx):
    # Only install the statically linked executable.
    build = ctx.extract().autoconf()
    build.make()
    build.make_install().path('sbin/pkg-static').install('sbin/pkg')

host_package(
    name='pkg',
    version='1.5.6',
    homepage='https://github.com/freebsd/pkg',
    maintainer='info@nuxi.nl',
    lib_depends={'libarchive'},
    build_cmd=build,
)

distfile(
    name='pkg-1.5.6.tar.xz',
    checksum='30c772e97e306ad85dcc652e2a9951ad49b0827337066f44dba5d91882ad92b1',
    master_sites={'http://files.etoilebsd.net/pkg/'},
    patches={'unset-timestamp'},
)
