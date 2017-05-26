# Copyright (c) 2015-2017 Nuxi, https://nuxi.nl/
#
# This file is distributed under a 2-clause BSD license.
# See the LICENSE file for details.


def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    headers = ctx.extract('cloudlibc/v0.75').path('src/include')

    sources = {
        'absvdi2.c', 'absvsi2.c', 'absvti2.c', 'adddf3.c', 'addsf3.c',
        'addtf3.c', 'addvdi3.c', 'addvsi3.c', 'addvti3.c', 'ashldi3.c',
        'ashlti3.c', 'ashrdi3.c', 'ashrti3.c', 'clear_cache.c',
        'clzdi2.c', 'clzsi2.c', 'clzti2.c', 'cmpdi2.c', 'cmpti2.c',
        'comparedf2.c', 'comparesf2.c', 'comparetf2.c', 'ctzdi2.c',
        'ctzsi2.c', 'ctzti2.c', 'divdc3.c', 'divdf3.c', 'divdi3.c',
        'divmoddi4.c', 'divmodsi4.c', 'divsc3.c', 'divsf3.c',
        'divsi3.c', 'divtf3.c', 'divti3.c', 'divxc3.c',
        'enable_execute_stack.c', 'eprintf.c', 'extenddftf2.c',
        'extendhfsf2.c', 'extendsfdf2.c', 'extendsftf2.c', 'ffsdi2.c',
        'ffsti2.c', 'fixdfdi.c', 'fixdfsi.c', 'fixdfti.c', 'fixsfdi.c',
        'fixsfsi.c', 'fixsfti.c', 'fixtfdi.c', 'fixtfsi.c',
        'fixunsdfdi.c', 'fixunsdfsi.c', 'fixunsdfti.c', 'fixunssfdi.c',
        'fixunssfsi.c', 'fixunssfti.c', 'fixunstfdi.c', 'fixunstfsi.c',
        'fixunsxfdi.c', 'fixunsxfsi.c', 'fixunsxfti.c', 'fixxfdi.c',
        'fixxfti.c', 'floatdidf.c', 'floatdisf.c', 'floatdixf.c',
        'floatsidf.c', 'floatsisf.c', 'floatsitf.c', 'floattidf.c',
        'floattisf.c', 'floattixf.c', 'floatundidf.c', 'floatundisf.c',
        'floatundixf.c', 'floatunsidf.c', 'floatunsisf.c',
        'floatunsitf.c', 'floatuntidf.c', 'floatuntisf.c',
        'floatuntixf.c', 'int_util.c', 'lshrdi3.c', 'lshrti3.c',
        'moddi3.c', 'modsi3.c', 'modti3.c', 'muldc3.c', 'muldf3.c',
        'muldi3.c', 'mulodi4.c', 'mulosi4.c', 'muloti4.c', 'mulsc3.c',
        'mulsf3.c', 'multf3.c', 'multi3.c', 'mulvdi3.c', 'mulvsi3.c',
        'mulvti3.c', 'mulxc3.c', 'negdf2.c', 'negdi2.c', 'negsf2.c',
        'negti2.c', 'negvdi2.c', 'negvsi2.c', 'negvti2.c',
        'paritydi2.c', 'paritysi2.c', 'parityti2.c', 'popcountdi2.c',
        'popcountsi2.c', 'popcountti2.c', 'powidf2.c', 'powisf2.c',
        'powitf2.c', 'powixf2.c', 'ppc/floatditf.c', 'ppc/gcc_qadd.c',
        'ppc/gcc_qmul.c', 'ppc/gcc_qsub.c', 'ppc/multc3.c', 'subdf3.c',
        'subsf3.c', 'subtf3.c', 'subvdi3.c', 'subvsi3.c', 'subvti3.c',
        'trampoline_setup.c', 'truncdfhf2.c', 'truncdfsf2.c',
        'truncsfhf2.c', 'trunctfdf2.c', 'trunctfsf2.c', 'ucmpdi2.c',
        'ucmpti2.c', 'udivdi3.c', 'udivmoddi4.c', 'udivmodsi4.c',
        'udivmodti4.c', 'udivsi3.c', 'udivti3.c', 'umoddi3.c',
        'umodsi3.c', 'umodti3.c', 'x86_64/floatdidf.c',
        'x86_64/floatdisf.c', 'x86_64/floatdixf.c',
        'x86_64/floatundidf.S', 'x86_64/floatundisf.S',
        'x86_64/floatundixf.S',
    }
    if ctx.cpu().startswith('armv'):
        sources |= {
            'arm/aeabi_idivmod.S', 'arm/aeabi_ldivmod.S',
            'arm/aeabi_uidivmod.S', 'arm/aeabi_uldivmod.S',
        }

    srcdir = root.path('lib/builtins')
    library = ctx.archive(srcdir.path(f).compile([
        '-I%s' % headers, '-DCRT_HAS_128BIT',
    ]) for f in sources)
    library.install('lib/libcompiler_rt.a')

package(
    name='compiler-rt',
    version='4.0.0',
    homepage='http://compiler-rt.llvm.org/',
    build_cmd=build,
)

distfile(
    name='compiler-rt-4.0.0.src.tar.xz',
    checksum='d3f25b23bef24c305137e6b44f7e81c51bbec764c119e01512a9bd2330be3115',
    master_sites={'http://www.llvm.org/releases/4.0.0/'},
)
