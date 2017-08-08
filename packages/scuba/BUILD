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
    version='0.1',
    homepage='https://github.com/NuxiNL/scuba',
    lib_depends={'arpc', 'cxx-runtime', 'flower', 'grpc', 'yaml-cpp'},
    build_cmd=build)

distfile(
    name='scuba/v0.1.tar.gz',
    checksum='d5ce680b98b1e4f3759cdcdbe0c3cedb5e2c2393b108f70be70ad87d179f6f58',
    master_sites={'https://github.com/NuxiNL/scuba/archive/'})
