# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.run(['./configure.py', '--bootstrap'])
    srcdir.path('ninja').install('bin/ninja')

host_package(
    name='ninja',
    version='1.7.1',
    homepage='https://ninja-build.org/',
    build_cmd=build,
)

distfile(
    name='ninja/v1.7.1.tar.gz',
    checksum='51581de53cf4705b89eb6b14a85baa73288ad08bff256e7d30d529155813be19',
    master_sites={'https://github.com/ninja-build/ninja/archive/'},
)
