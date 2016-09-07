# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure([
        '--with-pcre=system',
        'ac_cv_func_posix_getgrgid_r=no',
        'ac_cv_func_posix_getpwuid_r=no',
        'ac_cv_header_sys_resource_h=no',
        'glib_cv_stack_grows=' + {
            'down': 'no',
            'up': 'yes',
        }[ctx.stack_direction()],
        'glib_cv_value_MSG_DONTROUTE=undefined',
        'glib_cv_value_MSG_OOB=undefined',
        'glib_cv_value_POLLPRI=undefined',
    ])
    build.make(['bin_PROGRAMS='])
    stage = build.make_install(['bin_PROGRAMS=', 'install'])
    stage.path('bin/glib-gettextize').unhardcode_paths()
    stage.path('share/gdb').remove()
    stage.install()

package(
    name='glib',
    version='2.48.2',
    homepage='https://developer.gnome.org/glib/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libffi', 'pcre', 'zlib'},
    build_cmd=build,
)


def host_build(ctx):
    build = ctx.extract().gnu_configure(['--disable-dtrace'])
    build.make()
    build.make_install().install()

host_package(
    name='glib',
    version='2.48.2',
    homepage='https://developer.gnome.org/glib/',
    maintainer='info@nuxi.nl',
    lib_depends={'gettext'},
    build_cmd=host_build,
)

distfile(
    name='glib-2.48.2.tar.xz',
    checksum='f25e751589cb1a58826eac24fbd4186cda4518af772806b666a3f91f66e6d3f4',
    master_sites={'http://ftp.gnome.org/pub/gnome/sources/glib/2.48/'},
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
