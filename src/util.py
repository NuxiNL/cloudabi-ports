import os
import shutil


def copy_file(source, target, preserve_attributes):
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
        if preserve_attributes:
            shutil.copystat(source, target)
    else:
        # Bail out on anything else.
        raise Exception(source + ' is of an unsupported type')


def make_dir(path):
    try:
        os.makedirs(path)
    except:
        pass


def make_parent_dir(path):
    make_dir(os.path.dirname(path))


def remove(path):
    try:
        shutil.rmtree(path)
    except:
        os.unlink(path)


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
