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
    version='0.5',
    homepage='https://github.com/NuxiNL/scuba',
    lib_depends={'arpc', 'cxx-runtime', 'flower', 'grpc', 'yaml2argdata'},
    build_cmd=build)

distfile(
    name='scuba/v0.5.tar.gz',
    checksum='fb86345de9dd85ed0a2ef5c00c0760906fb27483436b8e4139c42e9a34355552',
    master_sites={'https://github.com/NuxiNL/scuba/archive/'})
