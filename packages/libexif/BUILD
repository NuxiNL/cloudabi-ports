# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

package(
    name='libexif',
    version='0.6.21',
    homepage='http://libexif.sourceforge.net/',
    lib_depends={'c-runtime'},
    build_cmd=build_autoconf_automake,
)

distfile(
    name='libexif-0.6.21.tar.bz2',
    checksum='16cdaeb62eb3e6dfab2435f7d7bccd2f37438d21c5218ec4e58efa9157d4d41a',
    master_sites=sites_sourceforge('libexif/libexif/0.6.21'),
    unsafe_string_sources={
        'libexif/canon/mnote-canon-entry.c',
        'libexif/exif-entry.c',
        'libexif/olympus/exif-mnote-data-olympus.c',
        'libexif/olympus/mnote-olympus-entry.c',
        'libexif/pentax/exif-mnote-data-pentax.c',
    },
)
