# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf([
        '--with-pcre=system',
        'ac_cv_func_posix_getgrgid_r=no',
        'ac_cv_func_posix_getpwuid_r=no',
        'glib_cv_stack_grows=' + {'aarch64': 'no', 'x86_64': 'no'}[ctx.cpu()],
        'glib_cv_value_MSG_DONTROUTE=undefined',
        'glib_cv_value_MSG_OOB=undefined',
        'glib_cv_value_POLLPRI=undefined',
    ])
    build.make(['bin_PROGRAMS='])
    build.make_install(['bin_PROGRAMS=', 'install']).install()

package(
    name='glib',
    version='2.46.2',
    homepage='https://developer.gnome.org/glib/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libffi', 'pcre', 'zlib'},
    build_cmd=build,
)


def host_build(ctx):
    build = ctx.extract().autoconf(['--disable-dtrace'])
    build.make()
    build.make_install().install()

host_package(
    name='glib',
    version='2.46.2',
    homepage='https://developer.gnome.org/glib/',
    maintainer='info@nuxi.nl',
    lib_depends={'gettext'},
    build_cmd=host_build,
)

distfile(
    name='glib-2.46.2.tar.xz',
    checksum='5031722e37036719c1a09163cc6cf7c326e4c4f1f1e074b433c156862bd733db',
    master_sites={'http://ftp.gnome.org/pub/gnome/sources/glib/2.46/'},
    unsafe_string_sources={
        'glib/gbacktrace.c',
        'glib/ggettext.c',
        'glib/gkeyfile.c',
        'glib/gmarkup.c',
        'glib/gmessages.c',
        'glib/gnulib/vasnprintf.c',
        'glib/goption.c',
        'glib/gtestutils.c',
        'glib/gtimezone.c',
        'glib/libcharset/localcharset.c',
        'gobject/gobject-query.c',
        'gobject/gtype.c',
    },
)
