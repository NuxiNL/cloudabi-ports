package(
    name='libmad',
    version='0.15.1b',
    homepage='http://www.underbit.com/products/mad/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime'},
    build_cmd=build_autoconf_automake,
)

distfile(
    name='libmad-0.15.1b.tar.gz',
    checksum='bbfac3ed6bfbc2823d3775ebb931087371e142bb0e9bb1bee51a76a6e0078690',
    master_sites=sites_sourceforge('mad/libmad/0.15.1b'),
    patches={
        'configure',
        'no-sprintf',
    },
)
