# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.run(['./configure.py', '--bootstrap'])
    srcdir.path('ninja').install('bin/ninja')

host_package(
    name='ninja',
    version='1.7.2',
    homepage='https://ninja-build.org/',
    build_cmd=build,
)

distfile(
    name='ninja/v1.7.2.tar.gz',
    checksum='2edda0a5421ace3cf428309211270772dd35a91af60c96f93f90df6bc41b16d9',
    master_sites={'https://github.com/ninja-build/ninja/archive/'},
)
