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
    version='0.3',
    homepage='https://github.com/NuxiNL/scuba',
    lib_depends={'arpc', 'cxx-runtime', 'flower', 'grpc', 'yaml2argdata'},
    build_cmd=build)

distfile(
    name='scuba/v0.3.tar.gz',
    checksum='b930845217ff735c220ed99085cd42e3e78981241293ce04add35704252d351f',
    master_sites={'https://github.com/NuxiNL/scuba/archive/'})
