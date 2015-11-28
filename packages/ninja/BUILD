# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')
    srcdir.run(['./configure.py', '--bootstrap'])
    srcdir.path('ninja').install('bin/ninja')

host_package(
    name='ninja',
    version='1.6.0',
    homepage='https://ninja-build.org/',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='ninja/v1.6.0.tar.gz',
    checksum='b43e88fb068fe4d92a3dfd9eb4d19755dae5c33415db2e9b7b61b4659009cde7',
    master_sites={'https://github.com/ninja-build/ninja/archive/'},
)
