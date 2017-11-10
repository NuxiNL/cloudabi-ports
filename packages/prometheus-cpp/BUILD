# Copyright (c) 2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s')

    # Remove the Exposer class for now, as it depends on a web server
    # library that has not been ported yet.
    for i in {
            'include/prometheus/exposer.h',
            'lib/exposer.cc',
            'lib/handler.cc',
            'lib/handler.h',
    }:
        srcdir.path(i).remove()

    build = srcdir.cmake()
    build.ninja()
    build.ninja_install().install()


package(
    name='prometheus-cpp',
    version='0.1.6',
    homepage='https://github.com/jupp0r/prometheus-cpp',
    lib_depends={'cxx-runtime', 'protobuf-cpp'},
    build_cmd=build)

distfile(
    name='prometheus-cpp/v0.1.6.tar.gz',
    checksum='52995a826d609eaca6a07e47db6afdf5450ab8cd0fb1a07c346ff3c7180095d4',
    master_sites={'https://github.com/jupp0r/prometheus-cpp/archive/'})
