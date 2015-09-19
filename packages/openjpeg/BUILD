# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)s/version.2.1').cmake([
        '-DBUILD_CODEC=NO', '-DBUILD_MJ2=NO',
    ])
    # build.run(['/usr/local/bin/bash'])
    build.make()
    build.make_install().install()

package(
    name='openjpeg',
    version='2.1.0',
    homepage='http://www.openjpeg.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='openjpeg/version.2.1.tar.gz',
    checksum='4afc996cd5e0d16360d71c58216950bcb4ce29a3272360eb29cadb1c8bce4efc',
    master_sites={'https://github.com/uclouvain/openjpeg/archive/'},
)
