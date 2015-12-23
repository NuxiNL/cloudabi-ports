# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # Also install Bash under the name 'sh'.
    build = ctx.extract().autoconf()
    build.make()
    stage = build.make_install()
    stage.path('bin/sh').symlink('bash')
    stage.install()

host_package(
    name='bash',
    version='4.3.30',
    homepage='https://www.gnu.org/software/bash/',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='bash-4.3.30.tar.gz',
    checksum='317881019bbf2262fb814b7dd8e40632d13c3608d2f237800a8828fbb8a640dd',
    master_sites=sites_gnu('bash'),
)
