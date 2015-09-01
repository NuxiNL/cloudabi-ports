def compiler_rt_build(ctx):
  ctx.insert_sources(0, '.')
  sources = {
      'absvdi2.c', 'absvsi2.c', 'absvti2.c', 'adddf3.c', 'addsf3.c',
      'addtf3.c', 'addvdi3.c', 'addvsi3.c', 'addvti3.c', 'ashldi3.c',
      'ashlti3.c', 'ashrdi3.c', 'ashrti3.c', 'clear_cache.c',
      'clzdi2.c', 'clzsi2.c', 'clzti2.c', 'cmpdi2.c', 'cmpti2.c',
      'comparedf2.c', 'comparesf2.c', 'ctzdi2.c', 'ctzsi2.c',
      'ctzti2.c', 'divdc3.c', 'divdf3.c', 'divdi3.c', 'divmoddi4.c',
      'divmodsi4.c', 'divsc3.c', 'divsf3.c', 'divsi3.c', 'divtf3.c',
      'divti3.c', 'divxc3.c', 'enable_execute_stack.c', 'eprintf.c',
      'extendhfsf2.c', 'extendsfdf2.c', 'ffsdi2.c', 'ffsti2.c',
      'fixdfdi.c', 'fixdfsi.c', 'fixdfti.c', 'fixsfdi.c', 'fixsfsi.c',
      'fixsfti.c', 'fixunsdfdi.c', 'fixunsdfsi.c', 'fixunsdfti.c',
      'fixunssfdi.c', 'fixunssfsi.c', 'fixunssfti.c', 'fixunsxfdi.c',
      'fixunsxfsi.c', 'fixunsxfti.c', 'fixxfdi.c', 'fixxfti.c',
      'floatdidf.c', 'floatdisf.c', 'floatdixf.c', 'floatsidf.c',
      'floatsisf.c', 'floattidf.c', 'floattisf.c', 'floattixf.c',
      'floatundidf.c', 'floatundisf.c', 'floatundixf.c',
      'floatunsidf.c', 'floatunsisf.c', 'floatuntidf.c',
      'floatuntisf.c', 'floatuntixf.c', 'int_util.c', 'lshrdi3.c',
      'lshrti3.c', 'moddi3.c', 'modsi3.c', 'modti3.c', 'muldc3.c',
      'muldf3.c', 'muldi3.c', 'mulodi4.c', 'mulosi4.c', 'muloti4.c',
      'mulsc3.c', 'mulsf3.c', 'multf3.c', 'multi3.c', 'mulvdi3.c',
      'mulvsi3.c', 'mulvti3.c', 'mulxc3.c', 'negdf2.c', 'negdi2.c',
      'negsf2.c', 'negti2.c', 'negvdi2.c', 'negvsi2.c', 'negvti2.c',
      'paritydi2.c', 'paritysi2.c', 'parityti2.c', 'popcountdi2.c',
      'popcountsi2.c', 'popcountti2.c', 'powidf2.c', 'powisf2.c',
      'powitf2.c', 'powixf2.c', 'subdf3.c', 'subsf3.c', 'subtf3.c',
      'subvdi3.c', 'subvsi3.c', 'subvti3.c', 'trampoline_setup.c',
      'truncdfhf2.c', 'truncdfsf2.c', 'truncsfhf2.c', 'ucmpdi2.c',
      'ucmpti2.c', 'udivdi3.c', 'udivmoddi4.c', 'udivmodsi4.c',
      'udivmodti4.c', 'udivsi3.c', 'udivti3.c', 'umoddi3.c',
      'umodsi3.c', 'umodti3.c', 'x86_64/floatdidf.c',
      'x86_64/floatdisf.c', 'x86_64/floatdixf.c',
      'x86_64/floatundidf.S', 'x86_64/floatundisf.S',
      'x86_64/floatundixf.S',
  }
  libcompiler_rt = ctx.link_library(ctx.compile(os.path.join('lib/builtins', f))
                                    for f in sources)

  ctx.install(libcompiler_rt, 'lib/libcompiler_rt.a')

package(
    name = 'compiler-rt',
    version = '3.7.0-rc3',
    homepage = 'http://compiler-rt.llvm.org/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'cloudlibc'},
    distfiles = ['compiler-rt-3.7.0rc3.src.tar.xz'],
    build_cmd = compiler_rt_build,
)

distfile(
    name = 'compiler-rt-3.7.0rc3.src.tar.xz',
    checksum = '0e822f587363c19e4d527a3f7c43eaf80ab14c1e057e9baa28337b69dc5a1a6b',
    master_sites = {'http://llvm.org/pre-releases/3.7.0/rc3/'},
)
