def libcxx_build(ctx):
  ctx.insert_sources(0, '.')
  ctx.insert_sources(1, 'libcxxabi')
  sources = {
      'algorithm.cpp', 'bind.cpp', 'chrono.cpp',
      'condition_variable.cpp', 'debug.cpp', 'exception.cpp',
      'future.cpp', 'hash.cpp', 'ios.cpp', 'iostream.cpp', 'locale.cpp',
      'memory.cpp', 'mutex.cpp', 'new.cpp', 'optional.cpp',
      'random.cpp', 'regex.cpp', 'shared_mutex.cpp', 'stdexcept.cpp',
      'string.cpp', 'strstream.cpp', 'system_error.cpp', 'thread.cpp',
      'typeinfo.cpp', 'utility.cpp', 'valarray.cpp'
  }
  libcxx = ctx.link_library(
      ctx.compile(
          os.path.join('src', f),
          ['-Iinclude', '-Ilibcxxabi/include', '-std=c++11',
           '-D_LIBCPP_BUILD_STATIC', '-DLIBCXX_BUILDING_LIBCXXABI'])
      for f in sources)

  ctx.install(libcxx, 'lib/libc++.a')
  ctx.remove('include/CMakeLists.txt')
  ctx.remove('include/support')
  ctx.install('include', 'include/c++/v1')

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
