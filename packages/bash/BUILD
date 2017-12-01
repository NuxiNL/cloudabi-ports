# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    # Also install Bash under the name 'sh'.
    build = ctx.extract().gnu_configure()
    build.make()
    stage = build.make_install()
    stage.path('bin/sh').symlink('bash')
    stage.install()


host_package(
    name='bash',
    version='4.4.12',
    homepage='https://www.gnu.org/software/bash/',
    build_cmd=build)

distfile(
    name='bash-4.4.12.tar.gz',
    checksum='57d8432be54541531a496fd4904fdc08c12542f43605a9202594fa5d5f9f2331',
    master_sites=sites_gnu('bash'))
