def host_binutils_build(ctx):
  ctx.insert_sources()
  for arch in ARCHITECTURES:
    ctx.run_autoconf([
        '--target=' + arch,
        '--disable-gdb',
        '--disable-nls',
        '--disable-werror',
        '--enable-deterministic-archives'])
    ctx.run_make('.', gnu_make=True)
    stage = ctx.run_make_install('.')

    # Remove extraneous '<arch>/bin' directory. We shouldn't keep
    # binaries from the host system in this directory.
    ctx.remove(os.path.join(stage, arch, 'bin'))
    ctx.remove(os.path.join(stage, 'share/info'))
    ctx.install(stage)

host_package(
    name = 'binutils',
    version = '2.25.1',
    homepage = 'http://www.gnu.org/software/binutils/',
    maintainer = 'info@nuxi.nl',
    build_cmd = host_binutils_build,
)

distfile(
    name = 'binutils-2.25.1.tar.bz2',
    checksum = 'b5b14added7d78a8d1ca70b5cb75fef57ce2197264f4f5835326b0df22ac9f22',
    master_sites = {'http://ftp.gnu.org/gnu/binutils/'},
    patches = {'binutils/patch-cloudabi'},
)
