def host_pkgconf_build(ctx):
    # This tool should only be used for cross building. Disable any access
    # to global system paths.
    stage = ctx.distfile().autoconf([
        '--with-pkg-config-dir=/nonexistent',
        '--with-system-libdir=/nonexistent',
        '--with-system-includedir=/nonexistent',
    ], inplace=True).make_install()

    # Add a symbolic link to 'pkg-config' for compatibility.
    stage.path('bin/pkg-config').symlink('pkgconf')
    stage.install()

host_package(
    name='pkgconf',
    version='0.9.12',
    homepage='https://github.com/pkgconf/pkgconf',
    maintainer='info@nuxi.nl',
    build_cmd=host_pkgconf_build,
)

distfile(
    name='pkgconf-0.9.12.tar.bz2',
    checksum='7ec8b516e655e247f4ba976837cee808134785819ab8f538f652fe919cc6c09f',
    master_sites={'http://rabbit.dereferenced.org/~nenolod/distfiles/'},
)
