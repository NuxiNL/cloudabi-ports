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
    name='scuba',
    version='0.4',
    homepage='https://github.com/NuxiNL/scuba',
    lib_depends={'arpc', 'cxx-runtime', 'flower', 'grpc', 'yaml2argdata'},
    build_cmd=build)

distfile(
    name='scuba/v0.4.tar.gz',
    checksum='d2d62e306f03d0f203cfe67ab583cb01cac3a0266d2fcb5d62f13e8cd2d55670',
    master_sites={'https://github.com/NuxiNL/scuba/archive/'})
