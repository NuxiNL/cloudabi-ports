# Copyright (c) 2016 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    # TODO(ed): Generalize the way we install Python code.
    srcdir = ctx.extract('Django-%(version)s')
    srcdir.path('django').install('lib/python3.6/django')

package(
    name='django',
    version='1.10.4',
    homepage='https://www.djangoproject.com/',
    lib_depends={'python'},
    build_cmd=build,
)

distfile(
    name='Django-1.10.4.tar.gz',
    checksum='fff7f062e510d812badde7cfc57745b7779edb4d209b2bc5ea8d954c22305c2b',
    master_sites={'https://www.djangoproject.com/m/releases/1.10/'},
)
