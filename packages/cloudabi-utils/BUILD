# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract()
    ctx.executable({
        root.path('src/cloudabi-reexec/cloudabi-reexec.c').compile(),
    }).install('libexec/cloudabi-reexec')

package(
    name='cloudabi-utils',
    version='0.5',
    homepage='https://github.com/NuxiNL/cloudabi-utils',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='cloudabi-utils-0.5.tar.xz',
    checksum='3d777f5c669a91f987151346f6ce8887f30865360ede4a844fa945d4877b2168',
    master_sites={'https://nuxi.nl/distfiles/cloudabi-utils/'},
)
