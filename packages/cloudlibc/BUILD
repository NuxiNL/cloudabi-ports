def cloudlibc_build(root):
  root.insert_sources()
  root.run(['./build'])

  root.run(['DESTDIR=stage', 'PREFIX=/', './install'])
  root.path('stage').install()

package(
    name = 'cloudlibc',
    version = '0.4',
    homepage = 'https://github.com/NuxiNL/cloudlibc',
    maintainer = 'info@nuxi.nl',
    build_cmd = cloudlibc_build,
)

distfile(
    name = 'cloudlibc-0.4.tar.xz',
    checksum = 'ec9892519a2c1711005f7ab7cc4d7f98278ab4f3fcce0466fe57bd4e902b06b1',
    master_sites = {'https://nuxi.nl/distfiles/cloudlibc/'},
    patches = {'cloudlibc/patch-atoi', 'cloudlibc/patch-ungetc'},
)
