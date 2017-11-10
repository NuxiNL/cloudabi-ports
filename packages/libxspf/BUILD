# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    root = ctx.extract()
    build = root.gnu_configure(['--disable-test'])
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'noinst_PROGRAMS=',
                        'install']).install()


package(
    name='libxspf',
    version='1.2.0',
    homepage='http://libspiff.sourceforge.net/',
    lib_depends={'cxx-runtime', 'expat', 'uriparser'},
    build_cmd=build)

distfile(
    name='libxspf-1.2.0.tar.bz2',
    checksum='ba9e93a0066469b074b4022b480004651ad3aa5b4313187fd407d833f79b43a5',
    master_sites=sites_sourceforge('libspiff/Sources/1.2.0'),
    unsafe_string_sources={
        'bindings/c/xspf_c.cpp',
        'src/XspfToolbox.cpp',
        'src/XspfXmlFormatter.cpp',
    })
