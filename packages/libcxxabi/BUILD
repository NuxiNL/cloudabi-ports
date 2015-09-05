def libcxxabi_build(ctx):
  root = ctx.distfile(0)
  ctx.distfile(1).rename(root.path('libunwind'))
  sources = {
      'abort_message.cpp', 'cxa_aux_runtime.cpp',
      'cxa_default_handlers.cpp', 'cxa_demangle.cpp',
      'cxa_exception.cpp', 'cxa_exception_storage.cpp', 'cxa_guard.cpp',
      'cxa_handlers.cpp', 'cxa_new_delete.cpp', 'cxa_personality.cpp',
      'cxa_thread_atexit.cpp', 'cxa_unexpected.cpp', 'cxa_vector.cpp',
      'cxa_virtual.cpp', 'exception.cpp', 'private_typeinfo.cpp',
      'stdexcept.cpp', 'typeinfo.cpp',
  }
  srcdir = root.path('src')
  libcxxabi = ctx.archive(
      srcdir.path(f).compile(
          ['-I../include', '-I../libunwind/include', '-std=c++11'])
      for f in sources)

  libcxxabi.install('lib/libc++abi.a')
  for f in {'include/cxxabi.h', 'include/__cxxabi_config.h'}:
    root.path(f).install(f)

package(
    name = 'libcxxabi',
    version = '3.7.0',
    homepage = 'http://libcxxabi.llvm.org/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c-runtime', 'libcxx'},
    distfiles = ['libcxxabi-3.7.0.src.tar.xz', 'libunwind-3.7.0.src.tar.xz'],
    build_cmd = libcxxabi_build,
)

distfile(
    name = 'libcxxabi-3.7.0.src.tar.xz',
    checksum = '48b074fd334958b2d8bab893c897a0c8258328782cdec2d229c7bce432b49beb',
    master_sites = {'http://llvm.org/releases/3.7.0/'},
)
