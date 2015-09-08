def build(ctx):
    build = ctx.extract('%(name)s_%(version)s').autoconf()
    build.make()
    build.make_install().install()

host_package(
    name='dpkg',
    version='1.18.2',
    homepage='https://www.debian.org/',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='dpkg_1.18.2.tar.xz',
    checksum='11484f2a73d027d696e720a60380db71978bb5c06cd88fe30c291e069ac457a4',
    master_sites=sites_debian('dpkg'),
    patches={'freebsd-build'},
)
