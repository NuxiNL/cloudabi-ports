# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
#
# SPDX-License-Identifier: BSD-2-Clause

import base64
import collections
import hashlib
import logging
import lzma
import math
import os
import re
import shutil
import stat
import subprocess
import time

from . import config
from . import rpm
from . import util
from .version import FullVersion, SimpleVersion

log = logging.getLogger(__name__)


class Catalog:
    def __init__(self, old_path, new_path):
        self._old_path = old_path
        self._new_path = new_path
        self._packages = set()

    @staticmethod
    def _get_suggested_mode(path):
        mode = os.lstat(path).st_mode
        if stat.S_ISLNK(mode):
            # Symbolic links.
            return 0o777
        elif stat.S_ISDIR(mode) or (mode & 0o111) != 0:
            # Directories and executable files.
            return 0o555
        else:
            # Non-executable files.
            return 0o444

    @staticmethod
    def _sanitize_permissions(directory, directory_mode=0o555):
        for root, dirs, files in os.walk(directory):
            util.lchmod(root, directory_mode)
            for filename in files:
                path = os.path.join(root, filename)
                util.lchmod(path, Catalog._get_suggested_mode(path))

    @staticmethod
    def _run_tar(args):
        subprocess.check_call(
            [os.path.join(config.DIR_BUILDROOT, 'bin/bsdtar')] + args)

    def insert(self, package, version, source):
        target = os.path.join(self._new_path,
                              self._get_filename(package, version))
        util.make_dir(self._new_path)
        util.remove(target)
        os.link(source, target)
        self._packages.add((package, version))

    def lookup_at_version(self, package, version):
        if self._old_path:
            path = os.path.join(self._old_path,
                                self._get_filename(package, version))
            if os.path.exists(path):
                return path
        return None


class DebianCatalog(Catalog):

    # List of official supported architectures obtained from
    # https://www.debian.org/ports/#portlist-released.
    _architectures = {
        'amd64', 'armel', 'armhf', 'i386', 'ia64', 'kfreebsd-amd64',
        'kfreebsd-i386', 'mips', 'mipsel', 'powerpc', 'ppc64el', 's390',
        's390x', 'sparc'
    }

    def __init__(self, old_path, new_path):
        super(DebianCatalog, self).__init__(old_path, new_path)

        # Scan the existing directory hierarchy to find the latest
        # version of all of the packages. We need to know this in order
        # to determine the Epoch and revision number for any new
        # packages we're going to build.
        self._existing = collections.defaultdict(FullVersion)
        if old_path:
            for root, dirs, files in os.walk(old_path):
                for filename in files:
                    parts = filename.split('_')
                    if len(parts) == 3 and parts[2] == 'all.deb':
                        name = parts[0]
                        version = FullVersion.parse_debian(parts[1])
                        if self._existing[name] < version:
                            self._existing[name] = version

    @staticmethod
    def _get_filename(package, version):
        return '%s_%s_all.deb' % (package.get_debian_name(),
                                  version.get_debian_version())

    @staticmethod
    def _get_control_snippet(package, version, installed_size=None):
        """Returns a string suitable for writing to a .deb control file.

        For the fields refer to the Debian Policy Manual
        https://www.debian.org/doc/debian-policy/ch-controlfields.html
        """
        snippet = ('Package: %(debian_name)s\n'
                   'Version: %(version)s\n'
                   'Architecture: all\n'
                   'Maintainer: %(maintainer)s\n'
                   'Description: %(name)s for %(arch)s\n'
                   'Homepage: %(homepage)s\n' % {
                       'arch': package.get_arch(),
                       'homepage': package.get_homepage(),
                       'maintainer': package.get_maintainer(),
                       'name': package.get_name(),
                       'debian_name': package.get_debian_name(),
                       'version': version.get_debian_version(),
                   })

        # Optional, estimate in kB of disk space needed to install the package
        if installed_size is not None:
            snippet += 'Installed-Size: %d\n' % math.ceil(
                installed_size / 1024)

        lib_depends = package.get_lib_depends()
        if lib_depends:
            snippet += 'Depends: %s\n' % ', '.join(
                sorted(dep.get_debian_name() for dep in lib_depends))
        return snippet

    def finish(self, private_key):
        # Create package index.
        def write_entry(f, package, version):
            f.write(self._get_control_snippet(package, version))
            filename = self._get_filename(package, version)
            path = os.path.join(self._new_path, filename)
            f.write('Filename: %s\n'
                    'Size: %u\n'
                    'SHA256: %s\n' % (filename, os.path.getsize(path),
                                      util.sha256(path).hexdigest()))

            f.write('\n')

        index = os.path.join(self._new_path, 'Packages')
        with open(index, 'wt') as f, lzma.open(index + '.xz', 'wt') as f_xz:
            for package, version in self._packages:
                write_entry(f, package, version)
                write_entry(f_xz, package, version)

        # Link the index into the per-architecture directory.
        for arch in self._architectures:
            index_arch = os.path.join(
                self._new_path,
                'dists/cloudabi/cloudabi/binary-%s/Packages' % arch)
            util.make_parent_dir(index_arch)
            os.link(index, index_arch)
            os.link(index + '.xz', index_arch + '.xz')
        checksum = util.sha256(index).hexdigest()
        checksum_xz = util.sha256(index + '.xz').hexdigest()
        size = os.path.getsize(index)
        size_xz = os.path.getsize(index + '.xz')
        os.unlink(index)
        os.unlink(index + '.xz')

        # Create the InRelease file.
        with open(
                os.path.join(self._new_path, 'dists/cloudabi/InRelease'),
                'w') as f, subprocess.Popen(
                    [
                        'gpg',
                        '--local-user',
                        private_key,
                        '--armor',
                        '--sign',
                        '--clearsign',
                        '--digest-algo',
                        'SHA256',
                    ],
                    stdin=subprocess.PIPE,
                    stdout=f) as proc:

            def append(text):
                proc.stdin.write(bytes(text, encoding='ASCII'))

            append('Suite: cloudabi\n'
                   'Components: cloudabi\n'
                   'Architectures: %s\n'
                   'Date: %s\n'
                   'SHA256:\n' %
                   (' '.join(sorted(self._architectures)),
                    time.strftime("%a, %d %b %Y %H:%M:%S UTC", time.gmtime())))
            for arch in sorted(self._architectures):
                append(' %s %d cloudabi/binary-%s/Packages\n' % (checksum,
                                                                 size, arch))
                append(' %s %d cloudabi/binary-%s/Packages.xz\n' %
                       (checksum_xz, size_xz, arch))

    def lookup_latest_version(self, package):
        return self._existing[package.get_debian_name()]

    def package(self, package, version):
        package.build()
        package.initialize_buildroot({'libarchive', 'llvm'})
        log.info('PKG %s', self._get_filename(package, version))

        rootdir = config.DIR_BUILDROOT
        debian_binary = os.path.join(rootdir, 'debian-binary')
        controldir = os.path.join(rootdir, 'control')
        datadir = os.path.join(rootdir, 'data')

        # Create 'debian-binary' file.
        with open(debian_binary, 'w') as f:
            f.write('2.0\n')

        # Create 'data.tar.xz' tarball that contains the files that need
        # to be installed by the package.
        prefix = os.path.join('/usr', package.get_arch())
        util.make_dir(datadir)
        package.extract(os.path.join(datadir, prefix[1:]), prefix)
        self._sanitize_permissions(datadir)
        self._run_tar([
            '-cJf',
            datadir + '.tar.xz',
            '-C',
            datadir,
            '.',
        ])

        # Create 'control.tar.gz' tarball that contains the control files.
        # We use .gz instead of .xz for the control file, since dpkg only supports
        # xz for control files since 1.17.6.
        util.make_dir(controldir)
        datadir_files = sorted(util.walk_files(datadir))
        datadir_size = sum(os.path.getsize(fpath) for fpath in datadir_files)
        with open(os.path.join(controldir, 'control'), 'w') as f:
            f.write(self._get_control_snippet(package, version, datadir_size))
        with open(os.path.join(controldir, 'md5sums'), 'w') as f:
            f.writelines('%s  %s\n' % (util.md5(fpath).hexdigest(
            ), os.path.relpath(fpath, datadir)) for fpath in datadir_files)
        self._sanitize_permissions(controldir)
        self._run_tar([
            '-czf',
            controldir + '.tar.gz',
            '--options',
            'gzip:!timestamp',
            '-C',
            controldir,
            '.',
        ])

        path = os.path.join(rootdir, 'output.txz')
        subprocess.check_call([
            os.path.join(rootdir, 'bin/llvm-ar'),
            'rc',
            path,
            debian_binary,
            controldir + '.tar.gz',
            datadir + '.tar.xz',
        ])
        return path


class FreeBSDCatalog(Catalog):
    def __init__(self, old_path, new_path):
        super(FreeBSDCatalog, self).__init__(old_path, new_path)

        # Scan the existing directory hierarchy to find the latest
        # version of all of the packages. We need to know this in order
        # to determine the Epoch and revision number for any new
        # packages we're going to build.
        self._existing = collections.defaultdict(FullVersion)
        if old_path:
            for root, dirs, files in os.walk(old_path):
                for filename in files:
                    parts = filename.rsplit('-', 1)
                    if len(parts) == 2 and parts[1].endswith('.txz'):
                        name = parts[0]
                        version = FullVersion.parse_freebsd(parts[1][:-4])
                        if self._existing[name] < version:
                            self._existing[name] = version

    @staticmethod
    def _get_filename(package, version):
        return '%s-%s.txz' % (package.get_freebsd_name(),
                              version.get_freebsd_version())

    def finish(self, private_key):
        subprocess.check_call([
            'pkg',
            'repo',
            self._new_path,
            private_key,
        ])
        # TODO(ed): Copy in some of the old files to keep clients happy.

    def lookup_latest_version(self, package):
        return self._existing[package.get_freebsd_name()]

    def package(self, package, version):
        package.build()
        package.initialize_buildroot({'libarchive'})
        log.info('PKG %s', self._get_filename(package, version))

        # The package needs to be installed in /usr/local/<arch> on the
        # FreeBSD system.
        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        arch = package.get_arch()
        prefix = os.path.join('/usr/local', arch)
        package.extract(installdir, prefix)
        files = sorted(util.walk_files(installdir))

        # Create the compact manifest.
        base_manifest = (
            '{"name":"%(freebsd_name)s",'
            '"origin":"devel/%(freebsd_name)s",'
            '"version":"%(version)s",'
            '"comment":"%(name)s for %(arch)s",'
            '"maintainer":"%(maintainer)s",'
            '"www":"%(homepage)s",'
            '"abi":"*",'
            '"arch":"*",'
            '"prefix":"/usr/local",'
            '"flatsize":%(flatsize)d,'
            '"desc":"%(name)s for %(arch)s"' % {
                'arch': arch,
                'flatsize': sum(os.lstat(path).st_size for path in files),
                'freebsd_name': package.get_freebsd_name(),
                'homepage': package.get_homepage(),
                'maintainer': package.get_maintainer(),
                'name': package.get_name(),
                'version': version.get_freebsd_version(),
            })
        deps = package.get_lib_depends()
        if deps:
            base_manifest += ',"deps":{%s}' % ','.join(
                '\"%s\":{"origin":"devel/%s","version":"0"}' % (dep, dep)
                for dep in sorted(pkg.get_freebsd_name() for pkg in deps))
        compact_manifest = os.path.join(config.DIR_BUILDROOT,
                                        '+COMPACT_MANIFEST')
        with open(compact_manifest, 'w') as f:
            f.write(base_manifest)
            f.write('}')

        # Create the fill manifest.
        if files:
            manifest = os.path.join(config.DIR_BUILDROOT, '+MANIFEST')
            with open(manifest, 'w') as f:
                f.write(base_manifest)
                f.write(',"files":{')
                f.write(','.join('"%s":"1$%s"' % (os.path.join(
                    prefix, os.path.relpath(path, installdir)), util.sha256(
                        path).hexdigest()) for path in files))
                f.write('}}')
        else:
            manifest = compact_manifest

        # Create the package.
        output = os.path.join(config.DIR_BUILDROOT, 'output.tar.xz')
        listing = os.path.join(config.DIR_BUILDROOT, 'listing')
        with open(listing, 'w') as f:
            # Leading files in tarball.
            f.write('#mtree\n')
            f.write(
                '+COMPACT_MANIFEST type=file mode=0644 uname=root gname=wheel time=0 contents=%s\n'
                % compact_manifest)
            f.write(
                '+MANIFEST type=file mode=0644 uname=root gname=wheel time=0 contents=%s\n'
                % manifest)
            for path in files:
                fullpath = os.path.join(prefix,
                                        os.path.relpath(path, installdir))
                if os.path.islink(path):
                    # Symbolic links.
                    f.write(
                        '%s type=link mode=0777 uname=root gname=wheel time=0 link=%s\n'
                        % (fullpath, os.readlink(path)))
                else:
                    # Regular files.
                    f.write(
                        '%s type=file mode=0%o uname=root gname=wheel time=0 contents=%s\n'
                        % (fullpath, self._get_suggested_mode(path), path))
        self._run_tar(['-cJf', output, '-C', installdir, '@' + listing])
        return output


class HomebrewCatalog(Catalog):

    _OSX_VERSIONS = {
        'el_capitan', 'high_sierra', 'mavericks', 'sierra', 'yosemite'
    }

    def __init__(self, old_path, new_path, url):
        super(HomebrewCatalog, self).__init__(old_path, new_path)
        self._url = url

        # Scan the existing directory hierarchy to find the latest
        # version of all of the packages. We need to know this in order
        # to determine the Epoch and revision number for any new
        # packages we're going to build.
        self._existing = collections.defaultdict(FullVersion)
        if old_path:
            for root, dirs, files in os.walk(old_path):
                for filename in files:
                    parts = filename.split('|', 1)
                    if len(parts) == 2:
                        name = parts[0]
                        version = FullVersion.parse_homebrew(parts[1])
                        if self._existing[name] < version:
                            self._existing[name] = version

    @staticmethod
    def _get_filename(package, version):
        return '%s|%s' % (package.get_homebrew_name(),
                          version.get_homebrew_version())

    @staticmethod
    def _get_classname(name):
        return ''.join(part.capitalize() for part in re.split('[-_]', name))

    def insert(self, package, version, source):
        super(HomebrewCatalog, self).insert(package, version, source)

        # Create symbolic to the tarball for every supported version of
        # Mac OS X.
        filename = self._get_filename(package, version)
        linksdir = os.path.join(self._new_path, 'links')
        util.make_dir(linksdir)
        for osx_version in self._OSX_VERSIONS:
            link = os.path.join(linksdir, '%s-%s.%s.bottle.tar.gz' %
                                (package.get_homebrew_name(),
                                 version.get_homebrew_version(), osx_version))
            util.remove(link)
            os.symlink(os.path.join('..', filename), link)

        # Create a formula.
        formulaedir = os.path.join(self._new_path, 'formulae')
        util.make_dir(formulaedir)
        with open(
                os.path.join(formulaedir, package.get_homebrew_name() + '.rb'),
                'w') as f:
            # Header.
            f.write("""class %(homebrew_class)s < Formula
  desc "%(name)s for %(arch)s"
  homepage "%(homepage)s"
  url "http://this.package.cannot.be.built.from.source/"
  version "%(version)s"
  revision %(revision)d
""" % {
                'arch':
                package.get_arch(),
                'homebrew_class':
                self._get_classname(package.get_homebrew_name()),
                'homepage':
                package.get_homepage(),
                'name':
                package.get_name(),
                'revision':
                version.get_revision(),
                'url':
                self._url,
                'version':
                version.get_version(),
            })

            # Dependencies.
            for dep in sorted(pkg.get_homebrew_name()
                              for pkg in package.get_lib_depends()):
                f.write('  depends_on "%s"\n' % dep)

            # Bottles: links to binary packages.
            f.write("""
  bottle do
    root_url "%(url)slinks"
""" % {
                'url': self._url,
            })
            sha256 = util.sha256(source).hexdigest()
            for osx_version in sorted(self._OSX_VERSIONS):
                f.write('    sha256 "%s" => :%s\n' % (sha256, osx_version))
            f.write('  end\nend\n')

    def lookup_latest_version(self, package):
        return self._existing[package.get_homebrew_name()]

    def package(self, package, version):
        package.build()
        package.initialize_buildroot({'libarchive'})
        log.info('PKG %s', self._get_filename(package, version))

        # The package needs to be installed in /usr/local/share/<arch>
        # on the Mac OS X system. In the tarball, pathnames need to be
        # prefixed with <name>/<version>.
        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        extractdir = os.path.join(installdir,
                                  package.get_homebrew_name(),
                                  version.get_homebrew_version())
        util.make_dir(extractdir)
        package.extract(
            os.path.join(extractdir, 'share', package.get_arch()),
            os.path.join('/usr/local/share', package.get_arch()))

        # Add a placeholder install receipt file. Homebrew depends on it
        # being present with at least these fields.
        with open(os.path.join(extractdir, 'INSTALL_RECEIPT.json'), 'w') as f:
            f.write('{"used_options":[],"unused_options":[]}\n')

        # Archive the results.
        self._sanitize_permissions(installdir, directory_mode=0o755)
        output = os.path.join(config.DIR_BUILDROOT, 'output.tar.gz')
        self._run_tar([
            '--options',
            'gzip:!timestamp',
            '-czf',
            output,
            '-C',
            installdir,
            package.get_homebrew_name(),
        ])
        return output


class NetBSDCatalog(Catalog):
    def __init__(self, old_path, new_path):
        super(NetBSDCatalog, self).__init__(old_path, new_path)

    @staticmethod
    def _get_filename(package, version):
        return '%s-%s.tgz' % (package.get_netbsd_name(),
                              version.get_netbsd_version())

    def lookup_latest_version(self, package):
        # TODO(ed): Implement repository scanning.
        return FullVersion()

    def package(self, package, version):
        package.build()
        package.initialize_buildroot({'libarchive'})
        log.info('PKG %s', self._get_filename(package, version))

        # The package needs to be installed in /usr/pkg/<arch> on the
        # NetBSD system.
        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        arch = package.get_arch()
        prefix = os.path.join('/usr/pkg', arch)
        package.extract(installdir, prefix)
        files = sorted(util.walk_files(installdir))

        # Package contents list.
        util.make_dir(installdir)
        with open(os.path.join(installdir, '+CONTENTS'), 'w') as f:
            f.write('@cwd /usr/pkg/%s\n'
                    '@name %s-%s\n' % (arch, package.get_netbsd_name(),
                                       version.get_netbsd_version()))
            for dep in sorted(pkg.get_netbsd_name()
                              for pkg in package.get_lib_depends()):
                f.write('@pkgdep %s-[0-9]*\n' % dep)
            for path in files:
                f.write(os.path.relpath(path, installdir) + '\n')

        # Package description.
        with open(os.path.join(installdir, '+COMMENT'), 'w') as f:
            f.write('%s for %s\n' % (package.get_name(), package.get_arch()))
        with open(os.path.join(installdir, '+DESC'), 'w') as f:
            f.write('%(name)s for %(arch)s\n'
                    '\n'
                    'Homepage:\n'
                    '%(homepage)s\n' % {
                        'arch': package.get_arch(),
                        'name': package.get_name(),
                        'homepage': package.get_homepage(),
                    })

        # Build information file.
        # TODO(ed): We MUST specify a machine architecture and operating
        # system, meaning that these packages are currently only
        # installable on NetBSD/x86-64. Figure out a way we can create
        # packages that are installable on any system that uses pkgsrc.
        with open(os.path.join(installdir, '+BUILD_INFO'), 'w') as f:
            f.write('MACHINE_ARCH=x86_64\n'
                    'PKGTOOLS_VERSION=00000000\n'
                    'OPSYS=NetBSD\n'
                    'OS_VERSION=\n')

        self._sanitize_permissions(installdir)
        output = os.path.join(config.DIR_BUILDROOT, 'output.tar.xz')
        listing = os.path.join(config.DIR_BUILDROOT, 'listing')
        with open(listing, 'w') as f:
            f.write('+CONTENTS\n+COMMENT\n+DESC\n+BUILD_INFO\n')
            for path in files:
                f.write(os.path.relpath(path, installdir) + '\n')
        self._run_tar(['-cJf', output, '-C', installdir, '-T', listing])
        return output


class OpenBSDCatalog(Catalog):
    def __init__(self, old_path, new_path):
        super(OpenBSDCatalog, self).__init__(old_path, new_path)

    @staticmethod
    def _get_filename(package, version):
        return '%s-%s.tgz' % (package.get_openbsd_name(),
                              version.get_openbsd_version())

    def lookup_latest_version(self, package):
        # TODO(ed): Implement repository scanning.
        return FullVersion()

    def package(self, package, version):
        package.build()
        package.initialize_buildroot({'libarchive'})
        log.info('PKG %s', self._get_filename(package, version))

        # The package needs to be installed in /usr/local/<arch> on the
        # OpenBSD system.
        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        arch = package.get_arch()
        prefix = os.path.join('/usr/local', arch)
        package.extract(installdir, prefix)
        files = sorted(util.walk_files(installdir))

        # Package contents list.
        contents = os.path.join(config.DIR_BUILDROOT, 'contents')
        with open(contents, 'w') as f:
            f.write('@name %s-%s\n'
                    '@cwd %s\n' % (package.get_openbsd_name(),
                                   version.get_openbsd_version(), prefix))
            # TODO(ed): Encode dependencies.
            written_dirs = set()
            for path in files:
                # Write entry for parent directories.
                relpath = os.path.relpath(path, installdir)
                fullpath = ''
                for component in os.path.dirname(relpath).split('/'):
                    fullpath += component + '/'
                    if fullpath not in written_dirs:
                        f.write(fullpath + '\n')
                        written_dirs.add(fullpath)

                if os.path.islink(path):
                    # Write entry for symbolic link.
                    f.write('%s\n'
                            '@symlink %s\n' % (relpath, os.readlink(path)))
                else:
                    # Write entry for regular file.
                    f.write('%s\n'
                            '@sha %s\n'
                            '@size %d\n' %
                            (relpath,
                             str(base64.b64encode(util.sha256(path).digest()),
                                 encoding='ASCII'), os.lstat(path).st_size))

        # Package description.
        desc = os.path.join(config.DIR_BUILDROOT, 'desc')
        with open(desc, 'w') as f:
            f.write('%(name)s for %(arch)s\n'
                    '\n'
                    'Maintainer: %(maintainer)s\n'
                    '\n'
                    'WWW:\n'
                    '%(homepage)s\n' % {
                        'arch': package.get_arch(),
                        'name': package.get_name(),
                        'maintainer': package.get_maintainer(),
                        'homepage': package.get_homepage(),
                    })

        output = os.path.join(config.DIR_BUILDROOT, 'output.tar.gz')
        listing = os.path.join(config.DIR_BUILDROOT, 'listing')
        with open(listing, 'w') as f:
            # Leading files in tarball.
            f.write('#mtree\n')
            f.write(
                '+CONTENTS type=file mode=0666 uname=root gname=wheel time=0 contents=%s\n'
                % contents)
            f.write(
                '+DESC type=file mode=0666 uname=root gname=wheel time=0 contents=%s\n'
                % desc)
            for path in files:
                relpath = os.path.relpath(path, installdir)
                if os.path.islink(path):
                    # Symbolic links need to use 0o555 on OpenBSD.
                    f.write(
                        '%s type=link mode=0555 uname=root gname=wheel time=0 link=%s\n'
                        % (relpath, os.readlink(path)))
                else:
                    # Regular files.
                    f.write(
                        '%s type=file mode=0%o uname=root gname=wheel time=0 contents=%s\n'
                        % (relpath, self._get_suggested_mode(path), path))
        self._run_tar([
            '--options',
            'gzip:!timestamp',
            '-czf',
            output,
            '-C',
            installdir,
            '@' + listing,
        ])
        return output


class ArchLinuxCatalog(Catalog):
    def __init__(self, old_path, new_path):
        super(ArchLinuxCatalog, self).__init__(old_path, new_path)

        self._existing = collections.defaultdict(FullVersion)
        if old_path:
            for root, dirs, files in os.walk(old_path):
                for filename in files:
                    parts = filename.rsplit('-', 3)
                    if len(parts) == 4 and parts[3] == 'any.pkg.tar.xz':
                        name = parts[0]
                        version = FullVersion.parse_archlinux(
                            '%s-%s' % (parts[1], parts[2]))
                        if self._existing[name] < version:
                            self._existing[name] = version

    @staticmethod
    def _get_filename(package, version):
        return '%s-%s-any.pkg.tar.xz' % (package.get_archlinux_name(),
                                         version.get_archlinux_version())

    @staticmethod
    def _get_suggested_mode(path):
        return Catalog._get_suggested_mode(path) | 0o200

    def lookup_latest_version(self, package):
        return self._existing[package.get_archlinux_name()]

    def package(self, package, version):
        package.build()
        package.initialize_buildroot({'libarchive'})
        log.info('PKG %s', self._get_filename(package, version))

        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        arch = package.get_arch()
        prefix = os.path.join('/usr', arch)
        package.extract(os.path.join(installdir, prefix[1:]), prefix)
        files = sorted(util.walk_files(installdir))

        util.make_dir(installdir)
        pkginfo = os.path.join(installdir, '.PKGINFO')
        with open(pkginfo, 'w') as f:
            f.write(
                'pkgname = %(archlinux_name)s\n'
                'pkgdesc = %(name)s for %(arch)s\n'
                'pkgver = %(version)s\n'
                'size = %(flatsize)s\n'
                'arch = any\n' % {
                    'arch': package.get_arch(),
                    'archlinux_name': package.get_archlinux_name(),
                    'flatsize': sum(os.lstat(path).st_size for path in files),
                    'name': package.get_name(),
                    'version': version.get_archlinux_version(),
                })
            lib_depends = package.get_lib_depends()
            for dep in sorted(pkg.get_archlinux_name()
                              for pkg in package.get_lib_depends()):
                f.write('depend = %s\n' % dep)
            for p in sorted(package.get_replaces()):
                f.write('conflict = %s-%s\n' % (arch, p))
            for p in sorted(package.get_replaces()):
                f.write('replaces = %s-%s\n' % (arch, p))

        output = os.path.join(config.DIR_BUILDROOT, 'output.tar.xz')
        listing = os.path.join(config.DIR_BUILDROOT, 'listing')
        with open(listing, 'w') as f:
            f.write('.PKGINFO\n')
            for path in files:
                f.write(os.path.relpath(path, installdir) + '\n')

        mtree = os.path.join(installdir, '.MTREE')

        with open(listing, 'w') as f:
            f.write('#mtree\n')
            f.write(
                '.PKGINFO type=file mode=0644 uname=root gname=root time=0 contents=%s\n'
                % pkginfo)
            f.write(
                '.MTREE type=file mode=0644 uname=root gname=root time=0 contents=%s\n'
                % mtree)
            for path in files:
                relpath = os.path.relpath(path, installdir)
                if os.path.islink(path):
                    f.write(
                        '%s type=link mode=0777 uname=root gname=root time=0 link=%s\n'
                        % (relpath, os.readlink(path)))
                else:
                    f.write(
                        '%s type=file mode=0%o uname=root gname=root time=0 contents=%s\n'
                        % (relpath, self._get_suggested_mode(path), path))

        self._run_tar([
            '-czf', mtree, '-C', installdir, '--format=mtree',
            '--options=gzip:!timestamp,!all,use-set,type,uid,gid,mode,time,size,md5,sha256,link',
            '--exclude=.MTREE', '@' + listing
        ])

        self._run_tar(['-cJf', output, '-C', installdir, '@' + listing])

        return output

    def finish(self, private_key):
        for package, version in self._packages:
            package_file = self._get_filename(package, version)
            subprocess.check_call([
                'gpg', '--detach-sign', '--local-user', private_key,
                '--no-armor', '--digest-algo', 'SHA256',
                os.path.join(self._new_path, package_file)
            ])
        db_file = os.path.join(self._new_path, 'cloudabi-ports.db.tar.xz')
        packages = [
            os.path.join(self._new_path, self._get_filename(*p))
            for p in self._packages
        ]
        # Ensure that repo-add as a valid working directory.
        os.chdir('/')
        subprocess.check_call(['repo-add', '-s', '-k', private_key, db_file] +
                              packages)


class CygwinCatalog(Catalog):
    def __init__(self, old_path, new_path):
        super(CygwinCatalog, self).__init__(old_path, new_path)

        self._existing = collections.defaultdict(FullVersion)
        if old_path:
            for root, dirs, files in os.walk(old_path):
                for filename in files:
                    if filename.endswith('.tar.xz'):
                        parts = filename[:-7].rsplit('-', 2)
                        if len(parts) == 3:
                            name = parts[0]
                            version = FullVersion.parse_cygwin(
                                '%s-%s' % (parts[1], parts[2]))
                            if self._existing[name] < version:
                                self._existing[name] = version

    @staticmethod
    def _get_filename(package, version):
        return '%s-%s.tar.xz' % (package.get_cygwin_name(),
                                 version.get_cygwin_version())

    def lookup_latest_version(self, package):
        return self._existing[package.get_cygwin_name()]

    def package(self, package, version):
        package.build()
        package.initialize_buildroot({'libarchive'})
        log.info('PKG %s', self._get_filename(package, version))

        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        arch = package.get_arch()
        prefix = os.path.join('/usr', arch)
        package.extract(os.path.join(installdir, prefix[1:]), prefix)
        files = sorted(util.walk_files(installdir))

        util.make_dir(installdir)
        output = os.path.join(config.DIR_BUILDROOT, 'output.tar.xz')
        self._run_tar(['-cJf', output, '-C', installdir, '.'])
        return output

    def finish(self, private_key):
        for cygwin_arch in ('x86', 'x86_64'):
            cygwin_arch_dir = os.path.join(self._new_path, cygwin_arch)
            util.make_dir(cygwin_arch_dir)
            setup_file = os.path.join(cygwin_arch_dir, 'setup.ini')
            with open(setup_file, 'w') as f:
                f.write('release: cygwin\n')
                f.write('arch: %s\n' % cygwin_arch)
                f.write('setup-timestamp: %d\n' % int(time.time()))
                for package, version in sorted(
                        self._packages, key=lambda p: p[0].get_cygwin_name()):
                    package_file_name = self._get_filename(package, version)
                    package_file = os.path.join(self._new_path,
                                                package_file_name)
                    f.write('\n'
                            '@ %(cygwinname)s\n'
                            'sdesc: "%(name)s for %(arch)s"\n'
                            'version: %(version)s\n'
                            'category: CloudABI\n' % {
                                'cygwinname': package.get_cygwin_name(),
                                'arch': package.get_arch(),
                                'name': package.get_name(),
                                'version': version.get_cygwin_version(),
                            })
                    if len(package.get_lib_depends()) > 0:
                        f.write('requires: %s\n' % ' '.join(
                            sorted(pkg.get_cygwin_name()
                                   for pkg in package.get_lib_depends())))
                    f.write('install: %(filename)s %(size)s %(sha512)s\n' % {
                        'size': os.lstat(package_file).st_size,
                        'filename': package_file_name,
                        'sha512': util.sha512(package_file).hexdigest(),
                    })
            subprocess.check_call([
                'gpg',
                '--sign',
                '--detach-sign',
                '--local-user',
                private_key,
                '--batch',
                '--yes',
                setup_file,
            ])


class RedHatCatalog(Catalog):
    def __init__(self, old_path, new_path):
        super(RedHatCatalog, self).__init__(old_path, new_path)

    @staticmethod
    def _get_filename(package, version):
        return '%s-%s.noarch.rpm' % (package.get_redhat_name(),
                                     version.get_redhat_version())

    @staticmethod
    def _file_linkto(filename):
        try:
            return os.readlink(filename)
        except OSError:
            return ''

    @staticmethod
    def _file_md5(filename):
        if os.path.islink(filename):
            return ''
        else:
            return util.md5(filename).hexdigest()

    @staticmethod
    def _file_mode(filename):
        mode = os.lstat(filename).st_mode
        if stat.S_ISLNK(mode):
            # Symbolic links.
            return 0o120777 - 65536
        elif stat.S_ISDIR(mode) or (mode & 0o111) != 0:
            # Directories and executable files.
            return 0o100555 - 65536
        else:
            # Non-executable files.
            return 0o100444 - 65536

    @staticmethod
    def _file_size(filename):
        sb = os.lstat(filename)
        if stat.S_ISREG(sb.st_mode):
            return sb.st_size
        return 0

    def lookup_latest_version(self, package):
        # TODO(ed): Implement repository scanning.
        return FullVersion()

    def package(self, package, version):
        package.build()
        package.initialize_buildroot({'libarchive'})
        log.info('PKG %s', self._get_filename(package, version))

        # The package needs to be installed in /usr/arch> on the Red Hat
        # system.
        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        arch = package.get_arch()
        prefix = os.path.join('/usr', arch)
        package.extract(installdir, prefix)
        files = sorted(util.walk_files(installdir))

        # Create an xz compressed cpio payload containing all files.
        listing = os.path.join(config.DIR_BUILDROOT, 'listing')
        with open(listing, 'w') as f:
            f.write('#mtree\n')
            for path in files:
                relpath = os.path.join(prefix,
                                       os.path.relpath(path, installdir))
                if os.path.islink(path):
                    f.write(
                        '%s type=link mode=0777 uname=root gname=root time=0 link=%s\n'
                        % (relpath, os.readlink(path)))
                else:
                    f.write(
                        '%s type=file mode=0%o uname=root gname=root time=0 contents=%s\n'
                        % (relpath, self._get_suggested_mode(path), path))
        data = os.path.join(config.DIR_BUILDROOT, 'data.cpio.xz')
        self._run_tar([
            '-cJf',
            data,
            '--format=newc',
            '-C',
            installdir,
            '@' + listing,
        ])

        # The header, based on the following documentation:
        # http://www.rpm.org/max-rpm/s1-rpm-file-format-rpm-file-format.html
        # http://refspecs.linux-foundation.org/LSB_5.0.0/LSB-Core-generic/LSB-Core-generic/pkgformat.html
        name = package.get_redhat_name()
        lib_depends = sorted(
            dep.get_redhat_name() for dep in package.get_lib_depends())
        dirs = sorted({os.path.dirname(f) for f in files})
        header = bytes(
            rpm.Header({
                100:
                rpm.StringArray(['C']),
                1000:
                rpm.String(name),
                1001:
                rpm.String(str(version.get_version())),
                1002:
                rpm.String(str(version.get_revision())),
                1003:
                rpm.Int32([version.get_epoch()]),
                1004:
                rpm.I18NString('%s for %s' % (name, arch)),
                1005:
                rpm.I18NString('%s for %s' % (name, arch)),
                1009:
                rpm.Int32([sum(self._file_size(f) for f in files)]),
                1014:
                rpm.String('Unknown'),
                1016:
                rpm.I18NString('Development/Libraries'),
                1020:
                rpm.String(package.get_homepage()),
                1021:
                rpm.String('linux'),
                1022:
                rpm.String('noarch'),
                1028:
                rpm.Int32(os.lstat(f).st_size for f in files),
                1030:
                rpm.Int16(self._file_mode(f) for f in files),
                1033:
                rpm.Int16(0 for f in files),
                1034:
                rpm.Int32(0 for f in files),
                1035:
                rpm.StringArray(self._file_md5(f) for f in files),
                1036:
                rpm.StringArray(self._file_linkto(f) for f in files),
                1037:
                rpm.Int32(0 for f in files),
                1039:
                rpm.StringArray('root' for f in files),
                1040:
                rpm.StringArray('root' for f in files),
                1047:
                rpm.StringArray([name]),
                1048:
                rpm.Int32(0 for dep in lib_depends),
                1049:
                rpm.StringArray(lib_depends),
                1050:
                rpm.StringArray('' for dep in lib_depends),
                1095:
                rpm.Int32(1 for f in files),
                1096:
                rpm.Int32(range(1, len(files) + 1)),
                1097:
                rpm.StringArray('' for f in files),
                1112:
                rpm.Int32(8 for dep in lib_depends),
                1113:
                rpm.StringArray([version.get_redhat_version()]),
                1116:
                rpm.Int32(dirs.index(os.path.dirname(f)) for f in files),
                1117:
                rpm.StringArray(os.path.basename(f) for f in files),
                1118:
                rpm.StringArray(
                    os.path.join(prefix, os.path.relpath(d, installdir)) + '/'
                    for d in dirs),
                1124:
                rpm.String('cpio'),
                1125:
                rpm.String('xz'),
                1126:
                rpm.String('9'),
            }))

        # The signature.
        checksum = hashlib.md5()
        checksum.update(header)
        util.hash_file(data, checksum)
        signature = bytes(
            rpm.Header({
                1000: rpm.Int32([len(header) + os.stat(data).st_size]),
                1004: rpm.Bin(checksum.digest()),
            }))

        # Create the RPM file.
        output = os.path.join(config.DIR_BUILDROOT, 'output.rpm')
        with open(output, 'wb') as f:
            # The lead.
            f.write(b'\xed\xab\xee\xdb\x03\x00\x00\x00\x00\x00')
            fullname = '%s-%s' % (name, version.get_redhat_version())
            f.write(bytes(fullname, encoding='ASCII')[:66].ljust(66, b'\0'))
            f.write(b'\x00\x01\x00\x05')
            f.write(b'\x00' * 16)

            # The signature, aligned up to eight bytes in size.
            f.write(signature)
            f.write(b'\0' * ((8 - len(signature) % 8) % 8))

            # The header.
            f.write(header)

            # The payload.
            with open(data, 'rb') as fin:
                shutil.copyfileobj(fin, f)
        return output

    def finish(self, private_key):
        subprocess.check_call(['createrepo', self._new_path])
        subprocess.check_call([
            'gpg',
            '--detach-sign',
            '--local-user',
            private_key,
            '--armor',
            os.path.join(self._new_path, 'repodata/repomd.xml'),
        ])
