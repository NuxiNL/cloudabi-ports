# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.path('yaml2argdata').install('include/yaml2argdata')


package(
    name='yaml2argdata',
    version='0.1',
    homepage='https://github.com/NuxiNL/yaml2argdata',
    lib_depends={'argdata', 'yaml-cpp'},
    build_cmd=build)

distfile(
    name='yaml2argdata/v0.1.tar.gz',
    checksum='64651c19ac3281054631595ecfe0f83f9d7a09ef5c8b1d1908b68b410fa2dc42',
    master_sites={'https://github.com/NuxiNL/yaml2argdata/archive/'})
