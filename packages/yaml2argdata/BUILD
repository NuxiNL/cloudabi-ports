# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('yaml2argdata').install('include/yaml2argdata')


package(
    name='yaml2argdata',
    version='0.3',
    homepage='https://github.com/NuxiNL/yaml2argdata',
    lib_depends={'argdata', 'yaml-cpp'},
    build_cmd=build)

distfile(
    name='yaml2argdata/v0.3.tar.gz',
    checksum='8b4d3bba51d0c7944dfe4c7d8c9cc8e49cb99f5b538195cc53ef49fd95519909',
    master_sites={'https://github.com/NuxiNL/yaml2argdata/archive/'})
