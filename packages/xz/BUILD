# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distrbuted under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    build = ctx.extract().autoconf([
        '--disable-lzmadec', '--disable-lzmainfo', '--disable-scripts',
        '--disable-xz', '--disable-xzdec',

        # Work around an issue on FreeBSD, where libmd's SHA256
        # functions causes checksum failures.
        'ac_cv_type_SHA256_CTX=no', 'ac_cv_search_SHA256_Init=no',
    ])
    build.make()
    build.make_install().install()

package(
    name='xz',
    version='5.2.2',
    homepage='http://tukaani.org/xz/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

host_package(
    name='xz',
    version='5.2.2',
    homepage='http://tukaani.org/xz/',
    maintainer='info@nuxi.nl',
    build_cmd=build,
)

distfile(
    name='xz-5.2.2.tar.xz',
    checksum='f341b1906ebcdde291dd619399ae944600edc9193619dd0c0110a5f05bfcc89e',
    master_sites={'http://tukaani.org/xz/'},
)
