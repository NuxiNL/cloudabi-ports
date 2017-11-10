# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    build = srcdir.cmake()
    build.ninja()
    build.ninja_install().install()


package(
    name='scuba',
    version='0.7',
    homepage='https://github.com/NuxiNL/scuba',
    lib_depends={'arpc', 'cxx-runtime', 'flower', 'grpc', 'yaml2argdata'},
    build_cmd=build)

distfile(
    name='scuba/v0.7.tar.gz',
    checksum='0453af283bb8247ab729c9f9bc4343e279326d0789ee0431711a3aa0111856b3',
    master_sites={'https://github.com/NuxiNL/scuba/archive/'})
