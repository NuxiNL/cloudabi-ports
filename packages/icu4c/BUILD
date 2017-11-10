# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    # The Linux configuration works all right in our case.
    srcdir = ctx.extract('%(name)s-60_1-src').path('source')
    srcdir.path('config/mh-unknown').symlink('mh-linux')

    # Build a copy of ICU for the host system.
    hostbuild = srcdir.host().gnu_configure()
    hostbuild.make()

    # Build a copy of ICU for the target system, providing it the
    # directory for the host build.
    build = srcdir.gnu_configure([
        '--disable-dyload',
        '--disable-extras',
        '--disable-samples',
        '--disable-shared',
        '--disable-tools',
        '--enable-static',
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
    version='60.1',
    homepage='http://site.icu-project.org/',
    lib_depends={'cxx-runtime'},
    build_cmd=build)

distfile(
    name='icu4c-60_1-src.tgz',
    checksum='f8f5a6c8fbf32c015a467972bdb1477dc5f5d5dfea908b6ed218715eeb5ee225',
    master_sites={'http://download.icu-project.org/files/icu4c/60.1/'},
    unsafe_string_sources={
        'source/common/cstring.h',
        'source/common/uloc.cpp',
        'source/i18n/choicfmt.cpp',
        'source/i18n/decNumber.cpp',
        'source/i18n/digitlst.cpp',
        'source/i18n/plurrule.cpp',
    })
