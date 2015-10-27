# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    for arch in ARCHITECTURES:
        build = root.autoconf([
            '--target=' + arch,
            '--disable-gdb',
            '--disable-nls',
            '--disable-werror',
            '--enable-deterministic-archives'])
        build.make()

        # Only install the linker and strip.
        stage = build.make_install()
        for bin in {'ld', 'strip'}:
            filename = 'bin/%s-%s' % (arch, bin)
            stage.path(filename).install(filename)
        filename = '%s/lib/ldscripts' % arch
        stage.path(filename).install(filename)

host_package(
    name='binutils',
    version='2.25.1',
    homepage='http://www.gnu.org/software/binutils/',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='binutils-2.25.1.tar.bz2',
    checksum='b5b14added7d78a8d1ca70b5cb75fef57ce2197264f4f5835326b0df22ac9f22',
    master_sites={'http://ftp.gnu.org/gnu/binutils/'},
)
