# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # Only install the statically linked executable.
    build = ctx.extract().autoconf()
    build.make()
    build.make_install().path('sbin/pkg-static').install('sbin/pkg')

host_package(
    name='pkg',
    version='1.6.0',
    homepage='https://github.com/freebsd/pkg',
    maintainer='info@nuxi.nl',
    lib_depends={'libarchive'},
    build_cmd=build,
)

distfile(
    name='pkg-1.6.0.tar.xz',
    checksum='ed8b651abaf613723bbec8363e7d1c4f8edfb487adb689d22880430026ab7912',
    master_sites={'http://files.etoilebsd.net/pkg/'},
)
