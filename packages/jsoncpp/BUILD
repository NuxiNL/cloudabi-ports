# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract('%(name)s/%(version)s').cmake([
        '-DJSONCPP_WITH_TESTS=OFF',
    ])
    build.ninja()
    build.ninja_install().install()


package(
    name='jsoncpp',
    version='1.8.3',
    homepage='https://github.com/open-source-parsers/jsoncpp',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='jsoncpp/1.8.3.tar.gz',
    checksum='3671ba6051e0f30849942cc66d1798fdf0362d089343a83f704c09ee7156604f',
    master_sites={'https://github.com/open-source-parsers/jsoncpp/archive/'},
    unsafe_string_sources={'src/lib_json/json_writer.cpp'})
