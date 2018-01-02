# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import os
import random

from . import config

from .builder import BuildHandle
from .distfile import Distfile
from .package import HostPackage, TargetPackage
from .version import SimpleVersion

from typing import Callable, Dict, NamedTuple, Optional, Set, Tuple


PackageInfo = NamedTuple('PackageInfo', [
    ('name', str),
    ('version', str),
    ('build_cmd', Callable[[BuildHandle], None]),
    ('build_depends', Optional[Set[str]]),
    ('lib_depends', Optional[Set[str]]),
    ('meta', Dict[str, str])])


class Repository:
    def __init__(self, install_directory: str) -> None:
        self._install_directory = install_directory

        self._distfiles = {}        # type: Dict[str, Distfile]
        self._host_packages = {}    # type: Dict[str, HostPackage]
        self._target_packages = {}  # type: Dict[Tuple[str, str], TargetPackage]

        self._deferred_host_packages = {}    # type: Dict[str, PackageInfo]
        self._deferred_target_packages = {}  # type: Dict[Tuple[str, str], PackageInfo]

    def add_build_file(self, path: str, distdir: str) -> None:
        def op_build_autoconf_automake(ctx):
            build = ctx.extract().gnu_configure()
            build.make()
            build.make_install().install()

        def op_distfile(**kwargs):
            # Determine canonical name by stripping the file extension.
            distfile = kwargs
            name = distfile['name']
            for ext in {
                    '.tar.bz2',
                    '.tar.gz',
                    '.tar.lzma',
                    '.tar.xz',
                    '.tgz',
                    '.zip',
            }:
                if distfile['name'].endswith(ext):
                    name = distfile['name'][:-len(ext)]
                    break

            # Automatically add patches if none are given.
            dirname = os.path.dirname(path)
            if 'patches' not in distfile:
                distfile['patches'] = (name[6:] for name in os.listdir(dirname)
                                       if name.startswith('patch-'))
            if 'unsafe_string_sources' not in distfile:
                distfile['unsafe_string_sources'] = frozenset()

            # Turn patch filenames into full paths.
            distfile['patches'] = {
                os.path.join(dirname, 'patch-' + patch)
                for patch in distfile['patches']
            }

            if name in self._distfiles:
                raise Exception('%s is redeclaring distfile %s' % (path, name))
            self._distfiles[name] = Distfile(distdir=distdir, **distfile)

        def op_host_package(**kwargs):
            package = kwargs
            package['resource_directory'] = os.path.dirname(path)
            name = package['name']
            if name in self._deferred_host_packages:
                raise Exception('%s is redeclaring packages %s' % (path, name))
            self._deferred_host_packages[name] = package

        def op_package(**kwargs):
            package = kwargs
            package['resource_directory'] = os.path.dirname(path)
            name = package['name']
            for arch in config.ARCHITECTURES:
                if (name, arch) in self._deferred_target_packages:
                    raise Exception('%s is redeclaring package %s/%s' %
                                    (path, arch, name))
                self._deferred_target_packages[(name, arch)] = package

        def op_sites_gnu(suffix):
            return {
                fmt + suffix + '/'
                for fmt in {
                    'http://ftp.gnu.org/gnu/',
                    'http://ftp.nluug.nl/gnu/',
                }
            }

        def op_sites_sourceforge(suffix):
            return {
                fmt + suffix + '/'
                for fmt in {
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
                }
            }

        identifiers = {
            'ARCHITECTURES': config.ARCHITECTURES,
            'build_autoconf_automake': op_build_autoconf_automake,
            'distfile': op_distfile,
            'host_package': op_host_package,
            'package': op_package,
            'sites_gnu': op_sites_gnu,
            'sites_sourceforge': op_sites_sourceforge,
        }

        with open(path, 'r') as f:
            exec(f.read(), identifiers, identifiers)

    def get_distfiles(self):
        return self._distfiles.values()

    def get_target_packages(self) -> Dict[Tuple[str, str], TargetPackage]:
        # Create host packages that haven't been instantiated yet.
        # This implicitly checks for dependency loops.
        def get_host_package(name):
            if name in self._deferred_host_packages:
                package = dict(self._deferred_host_packages.pop(name))
                if name in self._host_packages:
                    raise Exception('%s is declared multiple times' % name)
                build_depends = set()
                if 'build_depends' in package:
                    build_depends = {
                        get_host_package(dep)
                        for dep in package['build_depends']
                    }
                    del package['build_depends']
                lib_depends = set()
                if 'lib_depends' in package:
                    lib_depends = {
                        get_host_package(dep)
                        for dep in package['lib_depends']
                    }
                    del package['lib_depends']
                package['version'] = SimpleVersion(package['version'])
                self._host_packages[name] = HostPackage(
                    install_directory=os.path.join(self._install_directory,
                                                   'host', name),
                    distfiles=self._distfiles,
                    build_depends=build_depends,
                    lib_depends=lib_depends,
                    **package)
            return self._host_packages[name]

        while self._deferred_host_packages:
            get_host_package(
                random.sample(self._deferred_host_packages.keys(), 1)[0])

        # Create target packages that haven't been instantiated yet.
        def get_target_package(name, arch):
            if (name, arch) in self._deferred_target_packages:
                package = dict(
                    self._deferred_target_packages.pop((name, arch)))
                if (name, arch) in self._target_packages:
                    raise Exception('%s is declared multiple times' % name)
                lib_depends = set()
                if 'lib_depends' in package:
                    lib_depends = {
                        get_target_package(dep, arch)
                        for dep in package['lib_depends']
                    }
                    del package['lib_depends']
                package['version'] = SimpleVersion(package['version'])
                self._target_packages[(name, arch)] = TargetPackage(
                    install_directory=os.path.join(self._install_directory,
                                                   arch, name),
                    arch=arch,
                    distfiles=self._distfiles,
                    host_packages=self._host_packages,
                    lib_depends=lib_depends,
                    **package)
            return self._target_packages[(name, arch)]

        while self._deferred_target_packages:
            get_target_package(*random.sample(
                self._deferred_target_packages.keys(), 1)[0])

        # Generate per-architecture 'everything' meta packages. These
        # packages depend on all of the packages for one architecture.
        # They make it easier to install all packages at once.
        packages = self._target_packages.copy()
        for arch in config.ARCHITECTURES:
            packages[('everything', arch)] = TargetPackage(
                install_directory=os.path.join(self._install_directory, arch,
                                               'everything'),
                arch=arch,
                name='everything',
                version=SimpleVersion('1.0'),
                homepage='https://nuxi.nl/',
                host_packages=self._host_packages,
                lib_depends={
                    value
                    for key, value in self._target_packages.items()
                    if key[1] == arch
                },
                build_cmd=None,
                distfiles={},
                resource_directory=None)
        return packages
