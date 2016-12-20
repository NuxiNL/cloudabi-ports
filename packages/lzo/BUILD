# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract('%(name)s-2.09').gnu_configure()
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='lzo',
    version='2.9',
    homepage='http://www.oberhumer.com/opensource/lzo/',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='lzo-2.09.tar.gz',
    checksum='f294a7ced313063c057c504257f437c8335c41bfeed23531ee4e6a2b87bcb34c',
    master_sites={'http://www.oberhumer.com/opensource/lzo/download/'},
)
