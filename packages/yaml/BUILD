# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='yaml',
    version='0.1.7',
    homepage='http://pyyaml.org/wiki/LibYAML',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='yaml-0.1.7.tar.gz',
    checksum='8088e457264a98ba451a90b8661fcb4f9d6f478f7265d48322a196cec2480729',
    master_sites={'http://pyyaml.org/download/libyaml/'},
    unsafe_string_sources={'src/dumper.c'},
)
