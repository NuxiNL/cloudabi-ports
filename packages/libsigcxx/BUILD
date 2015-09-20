# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.

def build(ctx):
    build = ctx.extract('libsigc++-%(version)s').autoconf()
    build.make(['noinst_PROGRAMS='])
    build.make_install(['noinst_PROGRAMS=', 'install']).install()

package(
    name='libsigcxx',
    version='2.4.1',
    homepage='http://libsigc.sourceforge.net/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='libsigc++-2.4.1.tar.xz',
    checksum='540443492a68e77e30db8d425f3c0b1299c825bf974d9bfc31ae7efafedc19ec',
    master_sites={'http://ftp.gnome.org/pub/GNOME/sources/libsigc++/2.4/'},
)
