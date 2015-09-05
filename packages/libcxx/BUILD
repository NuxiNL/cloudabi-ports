def libcxx_build(ctx):
  root = ctx.distfile(0)
  ctx.distfile(1).rename(root.path('libcxxabi'))

  # Build libc++.a.
  sources = {
      'algorithm.cpp', 'bind.cpp', 'chrono.cpp',
      'condition_variable.cpp', 'debug.cpp', 'exception.cpp',
      'future.cpp', 'hash.cpp', 'ios.cpp', 'iostream.cpp', 'locale.cpp',
      'memory.cpp', 'mutex.cpp', 'new.cpp', 'optional.cpp',
      'random.cpp', 'regex.cpp', 'shared_mutex.cpp', 'stdexcept.cpp',
      'string.cpp', 'strstream.cpp', 'system_error.cpp', 'thread.cpp',
      'typeinfo.cpp', 'utility.cpp', 'valarray.cpp'
  }
  srcdir = root.path('src')
  libcxx = ctx.archive(
      srcdir.path(f).compile(
          ['-I../include', '-I../libcxxabi/include', '-std=c++11',
           '-D_LIBCPP_BUILD_STATIC', '-DLIBCXX_BUILDING_LIBCXXABI'])
      for f in sources)
  libcxx.install('lib/libc++.a')

  # Install header files.
  headers = root.path('include')
  headers.path('CMakeLists.txt').remove()
  headers.path('support').remove()
  headers.install('include/c++/v1')

package(
    name = 'libcxx',
    version = '3.7.0',
    homepage = 'http://libcxx.llvm.org/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c-runtime'},
    distfiles = ['libcxx-3.7.0.src.tar.xz', 'libcxxabi-3.7.0.src.tar.xz'],
    build_cmd = libcxx_build,
)

distfile(
    name = 'libcxx-3.7.0.src.tar.xz',
    checksum = 'c18f3c8333cd7e678c1424a57fe5e25efe740ca7caf62ac67152b4723f3ad08e',
    master_sites = {'http://llvm.org/releases/3.7.0/'},
    patches = {'libcxx/patch-no-std-funcs'},
)
