def libunwind_build(ctx):
  ctx.insert_sources(0, '.')
  c_sources = {
      'Unwind-sjlj.c', 'UnwindLevel1-gcc-ext.c', 'UnwindLevel1.c',
      'UnwindRegistersRestore.S', 'UnwindRegistersSave.S',
  }
  cxx_sources = {'Unwind-EHABI.cpp', 'libunwind.cpp'}
  libunwind = ctx.link_library(
      {ctx.compile(os.path.join('src', f), ['-Iinclude'])
       for f in c_sources} |
      {ctx.compile(os.path.join('src', f), ['-Iinclude', '-std=c++11'])
       for f in cxx_sources})

  ctx.install(libunwind, 'lib/libunwind.a')

package(
    name = 'libunwind',
    version = '3.7.0-rc3',
    homepage = 'http://libcxx.llvm.org/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c-runtime', 'libcxx'},
    distfiles = ['libunwind-3.7.0rc3.src.tar.xz'],
    build_cmd = libunwind_build,
)

distfile(
    name = 'libunwind-3.7.0rc3.src.tar.xz',
    checksum = '7a6defa868eca6d6db2a67b9eb1aec24236be60e2da64a22022306e931f4738b',
    master_sites = {'http://llvm.org/pre-releases/3.7.0/rc3/'},
)
