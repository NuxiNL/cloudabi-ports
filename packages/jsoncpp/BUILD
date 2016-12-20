# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)s/%(version)s').cmake([
        '-DJSONCPP_WITH_TESTS=OFF',
    ])
    build.ninja()
    build.ninja_install().install()

package(
    name='jsoncpp',
    version='1.8.0',
    homepage='https://github.com/open-source-parsers/jsoncpp',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='jsoncpp/1.8.0.tar.gz',
    checksum='5deb2462cbf0c0121c9d6c9823ec72fe71417e34242e3509bc7c003d526465bc',
    master_sites={'https://github.com/open-source-parsers/jsoncpp/archive/'},
    unsafe_string_sources={'src/lib_json/json_writer.cpp'},
)
