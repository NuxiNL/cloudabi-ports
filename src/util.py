# Copyright (c) 2015 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.

import gzip
import hashlib
import os
import shutil
import subprocess
import ssl
import urllib.request


def copy_file(source, target, preserve_attributes):
    if os.path.exists(target):
        raise Exception('About to overwrite %s with %s' % (source, target))
    if os.path.islink(source):
        # Preserve symbolic links.
        destination = os.readlink(source)
        if os.path.isabs(destination):
            raise Exception(
                '%s points to absolute location %s',
                source, destination)
        os.symlink(destination, target)
    elif os.path.isfile(source):
        # Copy regular files.
        shutil.copy(source, target)
        if preserve_attributes:
            shutil.copystat(source, target)
    else:
        # Bail out on anything else.
        raise Exception(source + ' is of an unsupported type')


def diff(orig_dir, patched_dir, patch):
    proc = subprocess.Popen(['diff', '-urN', orig_dir, patched_dir],
                            stdout=subprocess.PIPE)
    minline = bytes('--- %s/' % orig_dir, encoding='ASCII')
    plusline = bytes('+++ %s/' % patched_dir, encoding='ASCII')
    with open(patch, 'wb') as f:
        for l in proc.stdout.readlines():
            if l.startswith(b'diff '):
                # Omit lines that start with 'diff'. They serve
                # no purpose.
                pass
            elif l.startswith(minline):
                # Remove directory name and timestamp.
                f.write(b'--- ' + l[len(minline):].split(b'\t', 1)[0] +
                        b'\n')
            elif l.startswith(plusline):
                # Remove directory name and timestamp.
                f.write(b'+++ ' + l[len(plusline):].split(b'\t', 1)[0] +
                        b'\n')
                pass
            else:
                f.write(l)

def file_contents_equal(path1, path2):
    # Compare file contents.
    with open(path1, 'rb') as f1, open(path2, 'rb') as f2:
        while True:
            b1 = f1.read(16384)
            b2 = f2.read(16384)
            if b1 != b2:
                return False
            elif not b1:
                return True


def gzip_file(source, target):
    with open(source, 'rb') as f1, gzip.GzipFile(target, 'wb', mtime=0) as f2:
        shutil.copyfileobj(f1, f2)


def unsafe_fetch(url):
    # Fetch a file over HTTP, HTTPS or FTP. For HTTPS, we don't do any
    # certificate checking. The caller should validate the authenticity
    # of the result.
    try:
        # Python >= 3.4.3.
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return urllib.request.urlopen(url, context=ctx)
    except TypeError:
        # Python < 3.4.3.
        return urllib.request.urlopen(url)


def lchmod(path, mode):
    try:
        os.lchmod(path, mode)
    except AttributeError:
        if not os.path.islink(path):
            os.chmod(path, mode)


def make_dir(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def make_parent_dir(path):
    make_dir(os.path.dirname(path))


def _remove(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        pass
    except NotADirectoryError:
        os.unlink(path)


def remove(path):
    try:
        # First try to remove the file or directory directly.
        _remove(path)
    except PermissionError:
        # If that fails, add write permissions to the directories stored
        # inside and retry.
        for root, dirs, files in os.walk(path):
            os.chmod(root, 0o755)
        _remove(path)


def remove_and_make_dir(path):
    try:
        remove(path)
    except FileNotFoundError:
        pass
    make_dir(path)


def _hash_file(path, algorithm):
    checksum = algorithm()
    if os.path.islink(path):
        checksum.update(bytes(os.readlink(path), encoding='ASCII'))
    else:
        with open(path, 'rb') as f:
            while True:
                data = f.read(16384)
                if not data:
                    break
                checksum.update(data)
    return checksum


def sha256(path):
    return _hash_file(path, hashlib.sha256)


def md5(path):
    return _hash_file(path, hashlib.md5)


def walk_files(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            # Return all files.
            for f in files:
                yield os.path.join(root, f)
            # Return all symbolic links to directories as well.
            for f in dirs:
                fullpath = os.path.join(root, f)
                if os.path.islink(fullpath):
                    yield fullpath
    elif os.path.exists(path):
        yield path


def walk_files_concurrently(source, target):
    for source_filename in walk_files(source):
        target_filename = os.path.normpath(
            os.path.join(target, os.path.relpath(source_filename, source)))
        yield source_filename, target_filename
