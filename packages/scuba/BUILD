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
    version='0.6',
    homepage='https://github.com/NuxiNL/scuba',
    lib_depends={'arpc', 'cxx-runtime', 'flower', 'grpc', 'yaml2argdata'},
    build_cmd=build)

distfile(
    name='scuba/v0.6.tar.gz',
    checksum='02fd226b4640a913320f76a63a5555e1fbfcaf642d6e6aa9926187ee15ab8b68',
    master_sites={'https://github.com/NuxiNL/scuba/archive/'})
