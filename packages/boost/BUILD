# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # Build b2 for the host system.
    srcdir = ctx.extract('%(name)s_1_59_0')
    srcdir.host().run(['./bootstrap.sh', '--with-toolset=cc'])

    # Build Boost libraries.
    # TODO(ed): Implement this further.
    with srcdir.path('project-config.jam').open('w') as f:
        f.write('using gcc : cloudabi : %s ;\n' % ctx.cxx())
    with srcdir.diff('/home/edje/foo'):
        srcdir.debug_shell()
    srcdir.run([
        './b2', '-j8', 'link=static', 'toolset=gcc-cloudabi',
        '--without-python',
    ])

package(
    name='boost',
    version='1.59.0',
    homepage='http://www.boost.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'bzip2', 'cxx-runtime', 'icu4c', 'zlib'},
    build_cmd=build,
)

distfile(
    name='boost_1_59_0.tar.bz2',
    checksum='727a932322d94287b62abb1bd2d41723eec4356a7728909e38adb65ca25241ca',
    master_sites=sites_sourceforge('boost/boost/1.59.0'),
)
