# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.

package(
    name='libsodium',
    version='1.0.3',
    homepage='https://www.libsodium.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build_autoconf_automake,
)

distfile(
    name='libsodium-1.0.3.tar.gz',
    checksum='cbcfc63cc90c05d18a20f229a62c7e7054a73731d0aa858c0517152c549b1288',
    master_sites={'https://download.libsodium.org/libsodium/releases/'},
    patches={'arc4random'},
)
