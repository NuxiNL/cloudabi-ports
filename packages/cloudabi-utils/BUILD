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
    version='0.23',
    homepage='https://github.com/NuxiNL/cloudabi-utils',
    lib_depends={'c-runtime'},
    build_cmd=build,
    replaces={'cloudabi-reexec'},
)

distfile(
    name='cloudabi-utils/v0.23.tar.gz',
    checksum='f77bdb960c5d15446fa673fc9d88dc6db542620dc3c9114267726a90c2e4c689',
    master_sites={'https://github.com/NuxiNL/cloudabi-utils/archive/'},
)
