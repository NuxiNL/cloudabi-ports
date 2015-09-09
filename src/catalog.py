import os
import stat
import subprocess

from . import config
from . import util


class Catalog:

    def __init__(self, old_path, new_path):
        self._old_path = old_path
        self._new_path = new_path

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

    def insert(self, package, version, path):
        util.make_dir(self._new_path)
        os.link(
            path,
            os.path.join(self._new_path, self._get_filename(package, version)))

    def lookup_at_version(self, package, version):
        path = os.path.join(
            self._old_path,
            self._get_filename(package, version))
        return path if os.path.exists(path) else None

    def lookup_latest_version(self, package):
        # TODO(ed): Implement.
        return None


class DebianCatalog(Catalog):

    def __init__(self, old_path, new_path):
        super(DebianCatalog, self).__init__(old_path, new_path)

    @staticmethod
    def _get_filename(package, version):
        return '%s_%s_all.deb' % (
            package.get_debian_name(), version.get_debian())

    def finish(self):
        # TODO(ed): Implement.
        pass

    def package(self, package, version):
        package.build()
        # TODO(ed): Should this be public API?
        package._prepare_buildroot(set(['binutils', 'libarchive']), set())
        name = package.get_name()
        print('PKG', name, 'Debian')

        rootdir = config.DIR_BUILDROOT
        debian_binary = os.path.join(rootdir, 'debian-binary')
        controldir = os.path.join(rootdir, 'control')
        datadir = os.path.join(rootdir, 'data')

        # Create 'debian-binary' file.
        with open(debian_binary, 'w') as f:
            f.write('2.0\n')

        def tar(directory):
            # Reset permissions to sane values.
            for root, dirs, files in os.walk(directory):
                util.lchmod(root, 0o555)
                for filename in files:
                    path = os.path.join(root, filename)
                    util.lchmod(path, self._get_suggested_mode(path))

            # Create tarball.
            subprocess.check_call([
                os.path.join(rootdir, 'bin/bsdtar'),
                '-cJf', directory + '.tar.xz',
                '-C', directory,
                '.',
            ])

        # Create 'control.tar.gz' tarball that contains the control file.
        util.make_dir(controldir)
        arch = package.get_arch()
        with open(os.path.join(controldir, 'control'), 'w') as f:
            f.write(
                'Package: %(debian_name)s\n'
                'Version: %(version)s\n'
                'Architecture: all\n'
                'Maintainer: %(maintainer)s\n'
                'Description: %(name)s for %(arch)s\n'
                'Homepage: %(homepage)s\n' % {
                    'arch': arch,
                    'homepage': package.get_homepage(),
                    'maintainer': package.get_maintainer(),
                    'name': name,
                    'debian_name': package.get_debian_name(),
                    'version': version.get_debian(),
                })
            lib_depends = package.get_lib_depends()
            if lib_depends:
                f.write(
                    'Depends: %s\n' % ', '.join(sorted(
                        dep.get_debian_name() for dep in lib_depends)))
        tar(controldir)

        # Create 'data.tar.xz' tarball that contains the files that need
        # to be installed by the package.
        prefix = os.path.join('/usr', arch)
        util.make_dir(datadir)
        package.extract(os.path.join(datadir, prefix[1:]), prefix)
        tar(datadir)

        path = os.path.join(rootdir, 'output.txz')
        subprocess.check_call([
            os.path.join(rootdir, 'bin/x86_64-unknown-cloudabi-ar'),
            '-rc', path,
            debian_binary, controldir + '.tar.xz', datadir + '.tar.xz',
        ])
        return path


class FreeBSDCatalog(Catalog):

    def __init__(self, old_path, new_path):
        super(FreeBSDCatalog, self).__init__(old_path, new_path)

    @staticmethod
    def _get_filename(package, version):
        return '%s-%s.txz' % (package.get_freebsd_name(),
                              version.get_freebsd())

    def finish(self, private_key):
        subprocess.check_call([
            'pkg', 'repo', self._new_path, private_key,
        ])
        # TODO(ed): Copy in some of the old files to keep clients happy.

    def package(self, package, version):
        # Install just a copy of FreeBSD's pkg(8) into the buildroot,
        # which we can call into to create the package.
        package.build()
        # TODO(ed): Should this be public API?
        package._prepare_buildroot(set(['pkg']), set())
        name = package.get_name()
        print('PKG', name, 'FreeBSD')

        # The package needs to be installed in /usr/local/<arch> on the
        # FreeBSD system.
        arch = package.get_arch()
        prefix = os.path.join('/usr/local', arch)
        installdir = os.path.join(config.DIR_BUILDROOT, 'install')
        filesdir = os.path.join(installdir, prefix[1:])
        package.extract(filesdir, prefix)

        # Create a manifest file.
        util.make_dir(installdir)
        with open(os.path.join(installdir, '+MANIFEST'), 'w') as f:
            # Preamble.
            f.write(
                'name: %(freebsd_name)s\n'
                'version: \"%(version)s\"\n'
                'origin: devel/%(arch)s-%(name)s\n'
                'comment: %(name)s for %(arch)s\n'
                'www: %(homepage)s\n'
                'maintainer: %(maintainer)s\n'
                'prefix: /usr/local\n'
                'desc: %(name)s for %(arch)s\n'
                'abi: FreeBSD:*\n'
                'arch: freebsd:*\n' % {
                    'arch': arch,
                    'freebsd_name': package.get_freebsd_name(),
                    'homepage': package.get_homepage(),
                    'maintainer': package.get_maintainer(),
                    'name': name,
                    'version': version.get_freebsd(),
                })

            # Dependencies.
            f.write('deps: {\n')
            for dep in sorted(pkg.get_freebsd_name()
                              for pkg in package.get_lib_depends()):
                f.write(
                    '  \"%s\": {origin: devel/%s, version: 0}\n' %
                    (dep, dep))
            f.write('}\n')

            # Create entry for every file.
            f.write('files: {\n')
            for path in sorted(util.walk_files(filesdir)):
                f.write(
                    '  \"/%s\": { perm: 0%o }' % (
                        os.path.relpath(path, installdir),
                        self._get_suggested_mode(path)))
            f.write('}\n')

        # Create the package.
        subprocess.check_call([
            os.path.join(config.DIR_BUILDROOT, 'sbin/pkg'),
            'create',
            '-r', installdir,
            '-m', installdir,
            '-o', config.DIR_BUILDROOT,
        ])
        return os.path.join(
            config.DIR_BUILDROOT,
            self._get_filename(package, version))
