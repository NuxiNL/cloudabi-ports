# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # Also install Bash under the name 'sh'.
    build = ctx.extract().gnu_configure()
    build.make()
    stage = build.make_install()
    stage.path('bin/sh').symlink('bash')
    stage.install()

host_package(
    name='bash',
    version='4.4',
    homepage='https://www.gnu.org/software/bash/',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='bash-4.4.tar.gz',
    checksum='d86b3392c1202e8ff5a423b302e6284db7f8f435ea9f39b5b1b20fd3ac36dfcb',
    master_sites=sites_gnu('bash'),
)
