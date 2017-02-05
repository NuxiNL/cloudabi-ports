# Copyright (c) 2016-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('%(name)s/v%(version)s').path('src')
    cflags = ['-I%s' % srcdir.path('libemulator')]
    ctx.executable(
        srcdir.path(f).compile(cflags) for f in {
            'cloudabi-emulate/cloudabi-emulate.c',
            'libemulator/emulate.c',
            'libemulator/futex.c',
            'libemulator/posix.c',
            'libemulator/random.c',
            'libemulator/signals.c',
            'libemulator/str.c',
            'libemulator/tidpool.c',
            'libemulator/tls.c',
        }).install('bin/cloudabi-emulate')
    ctx.executable({
        srcdir.path('cloudabi-reexec/cloudabi-reexec.c').compile(),
    }).install('libexec/cloudabi-reexec')

package(
    name='cloudabi-utils',
    version='0.21',
    homepage='https://github.com/NuxiNL/cloudabi-utils',
    lib_depends={'c-runtime'},
    build_cmd=build,
    replaces={'cloudabi-reexec'},
)

distfile(
    name='cloudabi-utils/v0.21.tar.gz',
    checksum='e1a8f2b5d7677c1f39d96ee2b8f7750b950cd66e8e39cf18ef33a3d534df7265',
    master_sites={'https://github.com/NuxiNL/cloudabi-utils/archive/'},
)
