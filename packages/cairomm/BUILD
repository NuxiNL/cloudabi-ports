# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().gnu_configure()
    build.make()
    stage = build.make_install()
    stage.path('share/devhelp/books/cairomm-1.0/cairomm-1.0.devhelp2'
               ).unhardcode_paths()
    stage.install()


package(
    name='cairomm',
    version='1.12.0',
    homepage='http://cairographics.org/',
    lib_depends={'cairo', 'cxx-runtime', 'libsigcxx'},
    build_cmd=build)

distfile(
    name='cairomm-1.12.0.tar.gz',
    checksum='50435aec6fdd976934b791e808993160113ad19ca53a5634a9b64ccbe55874cc',
    master_sites={'http://cairographics.org/releases/'})
