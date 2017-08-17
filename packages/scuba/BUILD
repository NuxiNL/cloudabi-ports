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
    version='0.2',
    homepage='https://github.com/NuxiNL/scuba',
    lib_depends={'arpc', 'cxx-runtime', 'flower', 'grpc', 'yaml-cpp'},
    build_cmd=build)

distfile(
    name='scuba/v0.2.tar.gz',
    checksum='f322421a974c58072b54462c4942cd8c8a054c7c8aa3672633985ce2f0794df2',
    master_sites={'https://github.com/NuxiNL/scuba/archive/'})
