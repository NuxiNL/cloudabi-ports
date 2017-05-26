# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # Build b2 for the host system.
    srcdir = ctx.extract('%(name)s_1_61_0')
    srcdir.host().run(['./bootstrap.sh', '--with-toolset=cc'])

    # Build Boost libraries.
    with srcdir.path('project-config.jam').open('w') as f:
        f.write('using gcc : cloudabi : %s ;\n' % ctx.cxx())
    stage = srcdir.path('stage')
    srcdir.run([
        './b2', '-j8', '-d+2', 'binary-format=elf', 'link=static',
        'toolset=gcc-cloudabi', 'cxxflags=' + ctx.cxxflags(),
        '--without-python', '--prefix=%s' % stage, 'install',
    ] + {
        'armv6': ['abi=aapcs', 'address-model=32', 'architecture=arm'],
        'armv7': ['abi=aapcs', 'address-model=32', 'architecture=arm'],
        'aarch64': ['abi=aapcs', 'address-model=64', 'architecture=arm'],
        'i686': ['abi=sysv', 'address-model=32', 'architecture=x86'],
        'x86_64': ['abi=sysv', 'address-model=64', 'architecture=x86'],
    }[ctx.cpu()])
    stage.install()

package(
    name='boost',
    version='1.61.0',
    homepage='http://www.boost.org/',
    lib_depends={'bzip2', 'cxx-runtime', 'icu4c', 'zlib'},
    build_cmd=build,
)

distfile(
    name='boost_1_61_0.tar.bz2',
    checksum='a547bd06c2fd9a71ba1d169d9cf0339da7ebf4753849a8f7d6fdb8feee99b640',
    master_sites=sites_sourceforge('boost/boost/1.61.0'),
)
