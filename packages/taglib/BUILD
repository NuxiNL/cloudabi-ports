# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().cmake(['-DENABLE_STATIC=ON'])
    build.make()
    stage = build.make_install()
    stage.path('bin/taglib-config').unhardcode_paths()
    stage.install()

package(
    name='taglib',
    version='1.9.1',
    homepage='https://taglib.github.io/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime', 'zlib'},
    build_cmd=build,
)

distfile(
    name='taglib-1.9.1.tar.gz',
    checksum='72d371cd1419a87ae200447a53bff2be219283071e80fd12337928cc967dc71a',
    master_sites={'https://taglib.github.io/releases/'},
    patches={'no-fopen'},
)
