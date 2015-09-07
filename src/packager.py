from . import util


class Packager:

    def __init__(self, path):
        self._path = path

    def extract(self, target):
        for source_file, target_file in util.walk_files_concurrently(
                self._path, target):
            util.make_parent_dir(target_file)
            if target_file.endswith('.template'):
                # File is a template. Expand %%PREFIX%% tags.
                target_file = target_file[:-9]
                with open(source_file, 'r') as f:
                    contents = f.read()
                contents = contents.replace('%%PREFIX%%', target)
                with open(target_file, 'w') as f:
                    f.write(contents)
                shutil.copymode(source_file, target_file)
            else:
                # Regular file. Copy it over literally.
                print(source_file, target_file)
                util.copy_file(source_file, target_file, False)
