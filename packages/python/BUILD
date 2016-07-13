# Copyright (c) 2015 Nuxi, https://nuxi.nl/
# Copyright (c) 2016 Alex Willmer, alex@moreati.org.uk
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    srcdir = ctx.extract('Python-3.6.0a3')

    # Delete the in-tree copy of these, to make certain the out-of-tree
    # versions are used, i.e. those generated from our patched importlib
    srcdir.path('Python/importlib.h').remove()
    srcdir.path('Python/importlib_external.h').remove()

    # First build a native binary, this will be used by the cross-build
    # to generate some files (see also patch-makefile-regen)
    hostbuild = srcdir.host().gnu_configure()
    hostbuild.make()

    build = srcdir.gnu_configure([
        '--build=%s' % ctx.host().gnu_triple(),
        '--disable-shared',
        '--without-ensurepip',
        '--with-pydebug',
        '--without-threads',
        'ac_cv_buggy_getaddrinfo=no',
        'ac_cv_file__dev_ptc=no',
        'ac_cv_file__dev_ptmx=no',
        'ac_cv_have_long_long_format=yes',
        'CPPFLAGS=-static',
        'LDFLAGS=-static',
        'PYTHON_FOR_BUILD=_PYTHON_PROJECT_BASE=$(abs_builddir) '
        '_PYTHON_HOST_PLATFORM=$(_PYTHON_HOST_PLATFORM) '
        'PYTHONPATH=$(shell test -f pybuilddir.txt '
        '&& echo $(abs_builddir)/`cat pybuilddir.txt`:)'
        '$(srcdir)/Lib:'
        '$(srcdir)/Lib/$(PLATDIR) '
        '%s' % hostbuild.path('python'),
    ])
    build.make()
    stage = build.make_install()

    # Fix up pathnames in shebangs and build configurations.
    for f in {'bin/2to3-3.6', 'bin/idle3.6', 'bin/pydoc3.6',
              'bin/python3.6dm-config', 'bin/pyvenv-3.6',
              'lib/python3.6/lib-dynload/_sysconfigdata_m.py',
              'lib/python3.6/config-3.6dm/Makefile',
              'lib/python3.6/config-3.6dm/python-config.py'}:
        stage.path(f).unhardcode_paths()

    # Remove Pickle files, as they don't seem to be stable.
    for f in {'lib/python3.6/lib2to3/Grammar3.6.0.alpha.3.pickle',
              'lib/python3.6/lib2to3/PatternGrammar3.6.0.alpha.3.pickle'}:
        stage.path(f).remove()
    stage.install()

package(
    name='python',
    version='3.6.0',
    homepage='https://www.python.org/',
    maintainer='alex@moreati.org.uk',
    lib_depends={'c-runtime'},
    build_cmd=build,
)

distfile(
    name='Python-3.6.0a3.tar.xz',
    checksum='2cd0611c3456a83737d99d8ffd36d4094b3d44c29dd3a4185f1146be502a8321',
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
        'Modules/getpath.c',
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
