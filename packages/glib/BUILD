# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause


def build(ctx):
    build = ctx.extract().gnu_configure([
        '--with-pcre=system',
        'ac_cv_func_posix_getgrgid_r=no',
        'ac_cv_func_posix_getpwuid_r=no',
        'ac_cv_header_sys_resource_h=no',
        'ac_cv_lib_socket_socket=yes',
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
    version='2.50.3',
    homepage='https://developer.gnome.org/glib/',
    lib_depends={'c-runtime', 'libffi', 'pcre', 'zlib'},
    build_cmd=build)


def host_build(ctx):
    build = ctx.extract().gnu_configure(['--disable-dtrace'])
    build.make()
    build.make_install().install()


host_package(
    name='glib',
    version='2.50.3',
    homepage='https://developer.gnome.org/glib/',
    lib_depends={'gettext'},
    build_cmd=host_build)

distfile(
    name='glib-2.50.3.tar.xz',
    checksum='82ee94bf4c01459b6b00cb9db0545c2237921e3060c0b74cff13fbc020cfd999',
    master_sites={'http://ftp.gnome.org/pub/gnome/sources/glib/2.50/'},
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
    })
