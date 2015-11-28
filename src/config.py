# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

import platform
import os

# Architectures for which we can build packages.
ARCHITECTURES = {'aarch64-unknown-cloudabi', 'x86_64-unknown-cloudabi'}

# Temporary directory where packages will be built. This directory has
# to be fixed, as the compilation process tends to hardcode paths to the
# build directory. Debug symbols and __FILE__ use absolute paths.
DIR_BUILDROOT = '/usr/obj/cloudabi-ports'

# Location where resource files are stored.
DIR_RESOURCES = os.path.join(os.getcwd(), 'misc')

# Location at which distfiles can be fetched in case the master sites
# are down.
FALLBACK_MIRRORS = {'https://nuxi.nl/distfiles/third_party/'}

# Host C and C++ compiler, used to compile the build tools.
HOST_CC = '/usr/bin/cc'
HOST_CXX = '/usr/bin/c++'

# Name of the Perl executable.
PERL = ('/usr/local/bin/perl' if platform.system() == 'FreeBSD' else
        '/usr/bin/perl')
