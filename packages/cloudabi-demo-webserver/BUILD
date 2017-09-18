# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.cmake()
    build.ninja()
    build.ninja_install().install()


package(
    name='cloudabi-demo-webserver',
    version='0.1',
    homepage='https://github.com/NuxiNL/cloudabi-demo-webserver',
    lib_depends={'arpc', 'cxx-runtime', 'flower'},
    build_cmd=build)

distfile(
    name='cloudabi-demo-webserver/v0.1.tar.gz',
    checksum='091fe1cdd4c369edb0ae9d72d8427e8310d01c715fc57541243a6aeec702b016',
    master_sites={'https://github.com/NuxiNL/cloudabi-demo-webserver/archive/'})
