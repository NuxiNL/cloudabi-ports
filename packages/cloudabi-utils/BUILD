# Copyright (c) 2016 Nuxi, https://nuxi.nl/
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

    # TODO(ed): Integrate source file into cloudabi-utils.
    ctx.executable({
        ctx.resource('cloudabi-reexec.c').compile(),
    }).install('libexec/cloudabi-reexec')

package(
    name='cloudabi-utils',
    version='0.18',
    homepage='https://github.com/NuxiNL/cloudabi-utils',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='cloudabi-utils/v0.18.tar.gz',
    checksum='2aaf229ee09ec6ec42102bc36a28a5f18af5a278156e4e4feea36369b1ae621d',
    master_sites={'https://github.com/NuxiNL/cloudabi-utils/archive/'},
)
