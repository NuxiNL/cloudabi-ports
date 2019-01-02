# Copyright (c) 2017-2019 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('yaml2argdata').install('include/yaml2argdata')


package(
    name='yaml2argdata',
    version='0.4',
    homepage='https://github.com/NuxiNL/yaml2argdata',
    lib_depends={'argdata', 'yaml-cpp'},
    build_cmd=build)

distfile(
    name='yaml2argdata/v0.4.tar.gz',
    checksum='593dfcd923b4486e727fbb3442a1c4c5fa654eb259c9835e4f9f6c77cffe44d6',
    master_sites={'https://github.com/NuxiNL/yaml2argdata/archive/'})
