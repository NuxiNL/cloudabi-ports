# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('yaml2argdata').install('include/yaml2argdata')


package(
    name='yaml2argdata',
    version='0.2',
    homepage='https://github.com/NuxiNL/yaml2argdata',
    lib_depends={'argdata', 'yaml-cpp'},
    build_cmd=build)

distfile(
    name='yaml2argdata/v0.2.tar.gz',
    checksum='ee96a46b83e2259ab36db332bbd4d6d7ebf7a061ca9285786298ebedf9815997',
    master_sites={'https://github.com/NuxiNL/yaml2argdata/archive/'})
