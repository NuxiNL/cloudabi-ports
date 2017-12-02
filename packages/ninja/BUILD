# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.run(['./configure.py', '--bootstrap'])
    srcdir.path('ninja').install('bin/ninja')


host_package(
    name='ninja',
    version='1.8.2',
    homepage='https://ninja-build.org/',
    build_cmd=build)

distfile(
    name='ninja/v1.8.2.tar.gz',
    checksum='86b8700c3d0880c2b44c2ff67ce42774aaf8c28cbf57725cb881569288c1c6f4',
    master_sites={'https://github.com/ninja-build/ninja/archive/'})
