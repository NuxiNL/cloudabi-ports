#!/usr/bin/env python3

import fileinput
import hashlib
import os
import random
import shutil
import stat
import subprocess
import sys

from src.distfile import Distfile
from src import builder
from src import packager

# Fixed directories where we want to do the build and provide
# dependencies. These directories must not change, as this breaks the
# reproducibility of the generated packages.
DIR_BUILD = '/usr/obj/cloudabi-ports'

# Locations relative to the source tree.
DIR_ROOT = os.getcwd()
DIR_DISTFILES = os.path.join(DIR_ROOT, '_obj/distfiles')
DIR_INSTALL = os.path.join(DIR_ROOT, '_obj/install')
DIR_REPOSITORY = os.path.join(DIR_ROOT, 'packages')

PACKAGES = {}
HOST_PACKAGES = {}
PACKAGES_BUILT = set()
PACKAGES_BUILDING = set()

ARCHITECTURES = {'x86_64-unknown-cloudabi'}


def build_nothing(root):
    pass


def host_package(**kwargs):
    pkg = kwargs
    name = pkg['name']
    if name in HOST_PACKAGES:
        raise Exception('%s listed multiple times' % name)
    if 'distfiles' not in pkg:
        pkg['distfiles'] = ['%(name)s-%(version)s']
    pkg['distfiles'] = [filename % pkg for filename in pkg['distfiles']]
    HOST_PACKAGES[name] = pkg


def package(**kwargs):
    pkg = kwargs
    name = pkg['name']
    if name in PACKAGES:
        raise Exception('%s listed multiple times' % name)
    if 'distfiles' not in pkg:
        pkg['distfiles'] = ['%(name)s-%(version)s']
    pkg['distfiles'] = [filename % pkg for filename in pkg['distfiles']]
    if 'lib_depends' not in pkg:
        pkg['lib_depends'] = set()
    PACKAGES[name] = pkg

DISTFILES = {}


def distfile(**kwargs):
    distfile = kwargs

    # Determine canonical name by stripping the file extension.
    key = name = distfile['name']
    for ext in {'.tar.gz', '.tar.bz2', '.tar.xz'}:
        if name.endswith(ext):
            key = name[:-len(ext)]
            break

    if name in DISTFILES:
        raise Exception('%s listed multiple times' % name)
    DISTFILES[key] = Distfile(distdir=DIR_DISTFILES,
                              patchdir=DIR_REPOSITORY, **distfile)


def autoconf_automake_build(ctx):
    build = ctx.extract().autoconf()
    build.make()
    build.make_install().install()


def sourceforge_sites(suffix):
    return {fmt + suffix + '/' for fmt in {
        'http://downloads.sourceforge.net/project/',
        'http://freefr.dl.sourceforge.net/project/',
        'http://heanet.dl.sourceforge.net/project/',
        'http://internode.dl.sourceforge.net/project/',
        'http://iweb.dl.sourceforge.net/project/',
        'http://jaist.dl.sourceforge.net/project/',
        'http://kent.dl.sourceforge.net/project/',
        'http://master.dl.sourceforge.net/project/',
        'http://nchc.dl.sourceforge.net/project/',
        'http://ncu.dl.sourceforge.net/project/',
        'http://netcologne.dl.sourceforge.net/project/',
        'http://superb-dca3.dl.sourceforge.net/project/',
        'http://tenet.dl.sourceforge.net/project/',
        'http://ufpr.dl.sourceforge.net/project/',
    }}


def walk_files(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for f in files:
                yield (root, f)
    else:
        yield os.path.split(path)


def walk_files_concurrently(source, target):
    for dirname, filename in walk_files(source):
        source_filename = os.path.join(dirname, filename)
        target_filename = os.path.normpath(
            os.path.join(target, os.path.relpath(source_filename, source)))
        yield source_filename, target_filename

# Parse all of the BUILD rules.
for dirname, filename in walk_files(DIR_REPOSITORY):
    if filename == 'BUILD':
        with open(os.path.join(dirname, 'BUILD'), 'r') as f:
            exec(f.read())


def make_parents(path):
    try:
        os.makedirs(os.path.dirname(path))
    except:
        pass


def copy_file(source, target):
    if os.path.exists(target):
        raise Exception('About to overwrite %s with %s' % (source, target))
    if os.path.islink(source):
        # Preserve symbolic links.
        destination = os.readlink(source)
        if os.path.isabs(destination):
            raise Exception(
                '%s points to absolute location %s',
                source,
                destination)
        os.symlink(destination, target)
    elif os.path.isfile(source):
        # Copy regular files.
        shutil.copy(source, target)
    else:
        # Bail out on anything else.
        raise Exception(source + ' is of an unsupported type')


def _copy_dependencies(pkg, arch, done):
    for dep in pkg['lib_depends']:
        if dep not in done:
            packager.Packager(
                os.path.join(
                    DIR_INSTALL,
                    arch,
                    dep)).extract(
                os.path.join(
                    DIR_BUILD,
                    arch))
            done.add(dep)
            _copy_dependencies(PACKAGES[dep], arch, done)


def copy_dependencies(pkg, arch):
    _copy_dependencies(pkg, arch, set())


def build_package(pkg, arch):
    if pkg['name'] in PACKAGES_BUILT:
        return
    if pkg['name'] in PACKAGES_BUILDING:
        raise Exception('Cyclic dependency on package %s' % pkg['name'])
    PACKAGES_BUILDING.add(pkg['name'])
    for dep in pkg['lib_depends']:
        build_package(PACKAGES[dep], arch)

    try:
        shutil.rmtree(DIR_BUILD)
    except:
        pass

    install_directory = os.path.join(DIR_INSTALL, arch, pkg['name'])
    if 'build_cmd' in pkg and not os.path.isdir(install_directory):
        print('PKG', pkg['name'], arch)

        # Copy the toolchain into the build directory.
        for dep in HOST_PACKAGES:
            for source, target in walk_files_concurrently(
                    os.path.join(DIR_INSTALL, 'host', dep), DIR_BUILD):
                make_parents(target)
                copy_file(source, target)
        # Copy the dependencies into the build directory.
        copy_dependencies(pkg, arch)

        pkg['build_cmd'](builder.BuildHandle(builder.PackageBuilder(
            install_directory, arch), pkg['name'], pkg['version'], DISTFILES))

    PACKAGES_BUILDING.remove(pkg['name'])
    PACKAGES_BUILT.add(pkg['name'])


def build_host_package(pkg):
    try:
        shutil.rmtree(DIR_BUILD)
    except:
        pass
    install_directory = os.path.join(DIR_INSTALL, 'host', pkg['name'])
    if not os.path.isdir(install_directory):
        print('PKG', pkg['name'], 'host')
        pkg['build_cmd'](builder.BuildHandle(builder.HostPackageBuilder(
            install_directory), pkg['name'], pkg['version'], DISTFILES))

# Clean up.
try:
    os.makedirs(DIR_DISTFILES)
except:
    pass

if len(sys.argv) > 1:
    # Only build the packages provided on the command line.
    packages = set(sys.argv[1:])
    for pkg in packages:
        for arch in ARCHITECTURES:
            try:
                shutil.rmtree(os.path.join(DIR_INSTALL, arch, pkg))
            except:
                pass
    for pkg in packages:
        for arch in ARCHITECTURES:
            build_package(PACKAGES[pkg], arch)
else:
    # Build all packages.
    for pkg in HOST_PACKAGES:
        build_host_package(HOST_PACKAGES[pkg])
    for pkg in PACKAGES:
        for arch in ARCHITECTURES:
            build_package(PACKAGES[pkg], arch)
