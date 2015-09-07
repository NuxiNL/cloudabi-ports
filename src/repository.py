import os

from .distfile import Distfile


class Repository:

    def __init__(self):
        self._distfiles = {}

    def add_build_file(self, path, distdir):
        def op_autoconf_automake_build(ctx):
            build = ctx.extract().autoconf()
            build.make()
            build.make_install().install()

        def op_distfile(**kwargs):
            # Determine canonical name by stripping the file extension.
            distfile = kwargs
            key = name = distfile['name']
            for ext in {'.tar.gz', '.tar.bz2', '.tar.xz'}:
                if name.endswith(ext):
                    key = name[:-len(ext)]
                    break

            # Turn patch filenames into full paths.
            if 'patches' in distfile:
                distfile['patches'] = {
                    os.path.join(
                        os.path.dirname(path),
                        'patch-' + patch) for patch in distfile['patches']}

            if name in self._distfiles:
                raise Exception('%s is redeclaring distfile %s' % (path, name))
            self._distfiles[key] = Distfile(
                distdir=distdir,
                **distfile
            )

        def op_host_package(**kwargs):
            pass

        def op_package(**kwargs):
            pass

        def op_sourceforge_sites(suffix):
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

        identifiers = {
            'autoconf_automake_build': op_autoconf_automake_build,
            'distfile': op_distfile,
            'host_package': op_host_package,
            'package': op_package,
            'sourceforge_sites': op_sourceforge_sites,
        }

        with open(path, 'r') as f:
            exec(f.read(), identifiers, identifiers)

    def get_distfiles(self):
        return self._distfiles
