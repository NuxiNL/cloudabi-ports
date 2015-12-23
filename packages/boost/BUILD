# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # Build b2 for the host system.
    srcdir = ctx.extract('%(name)s_1_60_0')
    srcdir.host().run(['./bootstrap.sh', '--with-toolset=cc'])

    # Build Boost libraries.
    with srcdir.path('project-config.jam').open('w') as f:
        f.write('using gcc : cloudabi : %s ;\n' % ctx.cxx())
    stage = srcdir.path('stage')
    srcdir.run([
        './b2', '-j8', 'binary-format=elf', 'link=static',
        'toolset=gcc-cloudabi', '--without-python', '--prefix=%s' % stage,
        'install',
    ] + {
        'aarch64': ['abi=aapcs', 'address-model=64', 'architecture=arm'],
        'x86_64': ['abi=sysv', 'address-model=64', 'architecture=x86'],
    }[ctx.cpu()])
    stage.install()

package(
    name='boost',
    version='1.60.0',
    homepage='http://www.boost.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'bzip2', 'cxx-runtime', 'icu4c', 'zlib'},
    build_cmd=build,
)

distfile(
    name='boost_1_60_0.tar.bz2',
    checksum='686affff989ac2488f79a97b9479efb9f2abae035b5ed4d8226de6857933fd3b',
    master_sites=sites_sourceforge('boost/boost/1.60.0'),
)
