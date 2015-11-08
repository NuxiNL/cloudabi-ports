# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # The Linux configuration works all right in our case.
    srcdir = ctx.extract('%(name)s-55_1-src').path('source')
    srcdir.path('config/mh-unknown').symlink('mh-linux')

    # Build a copy of ICU for the host system.
    hostbuild = srcdir.host().autoconf()
    hostbuild.make()

    # Build a copy of ICU for the target system, providing it the
    # directory for the host build.
    build = srcdir.autoconf([
        '--disable-dyload', '--disable-extras', '--disable-samples',
        '--disable-shared', '--disable-tools', '--enable-static',
        '--with-cross-build=%s' % hostbuild,
    ])
    build.make()
    stage = build.make_install()
    stage.path('bin/icu-config').unhardcode_paths()
    stage.path('lib/icu/current/Makefile.inc').unhardcode_paths()
    stage.path('lib/icu/current/pkgdata.inc').unhardcode_paths()
    stage.install()

package(
    name='icu4c',
    version='55.1',
    homepage='http://site.icu-project.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'cxx-runtime'},
    build_cmd=build,
)

distfile(
    name='icu4c-55_1-src.tgz',
    checksum='e16b22cbefdd354bec114541f7849a12f8fc2015320ca5282ee4fd787571457b',
    master_sites={'http://download.icu-project.org/files/icu4c/55.1/'},
    unsafe_string_sources={
        'source/common/uloc.cpp',
        'source/i18n/choicfmt.cpp',
        'source/i18n/digitlst.cpp',
        'source/i18n/plurrule.cpp',
        'source/i18n/decNumber.c',
    },
)
