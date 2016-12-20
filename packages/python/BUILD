# Copyright (c) 2015-2016 Nuxi, https://nuxi.nl/
# Copyright (c) 2016 Alex Willmer, alex@moreati.org.uk
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('Python-3.6.0b4')

    # Delete the in-tree copy of these, to make certain the out-of-tree
    # versions are used, i.e. those generated from our patched importlib.
    generated_files = {'Python/importlib.h', 'Python/importlib_external.h'}
    for i in generated_files:
        srcdir.path(i).remove()

    # First build a native binary, this will be used by the cross-build
    # to generate some files.
    hostbuild = srcdir.host().gnu_configure()
    hostbuild.make()

    # For the target build, copy over the generated files into the build
    # directory, as generating them depends on tools built for the host.
    for f in {'Setup.dist', 'faulthandler.c', 'getpath.c', 'signalmodule.c'}:
        ctx.resource(f).rename(srcdir.path('Modules').path(f))
    build = srcdir.gnu_configure([
        '--build=%s' % ctx.host().gnu_triple(),
        '--disable-shared',
        '--without-ensurepip',
        '--with-pydebug',
        '--with-system-expat',
        '--with-system-ffi',
        'ac_cv_buggy_getaddrinfo=no',
        'ac_cv_file__dev_ptc=no',
        'ac_cv_file__dev_ptmx=no',
        'ac_cv_have_long_long_format=yes',
        'CPPFLAGS=-static',
        'LDFLAGS=-static',
        'READELF=false',
        'PYTHON_FOR_BUILD=_PYTHON_PROJECT_BASE=$(abs_builddir) '
        '_PYTHON_HOST_PLATFORM=$(_PYTHON_HOST_PLATFORM) '
        'PYTHONPATH=$(shell test -f pybuilddir.txt '
        '&& echo $(abs_builddir)/`cat pybuilddir.txt`:)'
        '$(srcdir)/Lib:'
        '$(srcdir)/Lib/$(PLATDIR) '
        '%s' % hostbuild.path('python'),
    ])
    for i in generated_files:
        hostbuild.path(i).rename(build.path(i))
    build.make()
    stage = build.make_install()

    # Fix up pathnames in shebangs and build configurations.
    for f in {'bin/2to3-3.6', 'bin/idle3.6', 'bin/pydoc3.6',
              'bin/python3.6dm-config', 'bin/pyvenv-3.6',
              'lib/python3.6/config-3.6dm/Makefile',
              'lib/python3.6/config-3.6dm/python-config.py'}:
        stage.path(f).unhardcode_paths()

    # Remove Pickle files, as they don't seem to be stable.
    for f in {'lib/python3.6/lib2to3/Grammar3.6.0.beta.1.pickle',
              'lib/python3.6/lib2to3/PatternGrammar3.6.0.beta.1.pickle'}:
        stage.path(f).remove()

    # TODO(ed): Figure out what to do with this!
    stage.path(
        'lib/python3.6/lib-dynload/_sysconfigdata_m_freebsd10_.py'
    ).remove()
    stage.install()

package(
    name='python',
    version='3.6.0',
    homepage='https://www.python.org/',
    lib_depends={
        'bzip2',
        'c-runtime',
        'expat',
        'libffi',
        'libressl',
        'xz',
        'zlib'
    },
    build_cmd=build,
)

distfile(
    name='Python-3.6.0b4.tar.xz',
    checksum='0afca41351ce9586becd398120ad2718252f93fffc134761c8fd80dc5144a979',
    master_sites={'https://www.python.org/ftp/python/3.6.0/'},
    unsafe_string_sources={
        'Modules/_ctypes/_ctypes.c',
        'Modules/_ctypes/_ctypes_test.c',
        'Modules/_datetimemodule.c',
        'Modules/_decimal/_decimal.c',
        'Modules/_decimal/libmpdec/io.c',
        'Modules/_elementtree.c',
        'Modules/_multiprocessing/semaphore.c',
        'Modules/_testbuffer.c',
        'Modules/_testcapimodule.c',
        'Modules/cjkcodecs/cjkcodecs.h',
        'Modules/main.c',
        'Modules/posixmodule.c',
        'Modules/pyexpat.c',
        'Modules/unicodedata.c',
        'Objects/bytesobject.c',
        'Objects/memoryobject.c',
        'Objects/structseq.c',
        'Objects/typeobject.c',
        'Objects/unicodeobject.c',
        'Parser/parsetok.c',
        'Parser/tokenizer.c',
        'Python/ast.c',
        'Python/codecs.c',
        'Python/pystrtod.c',
        'Python/traceback.c',
    },
)
