# The CloudABI Ports Collection

The CloudABI Ports Collection is a set of recipes that allow you to
cross compile and package a variety of Open Source libraries (and
utilities) for [CloudABI](https://github.com/NuxiNL/cloudlibc). These
packages are very useful when developing your own applications for
CloudABI. You will no longer need to figure out how to get the libraries
that your application depends on to build. You can simply obtain them
from this collection.

This collection only contains software that is cross compiled for
CloudABI. It does not offer packages for any native executables for your
operating system, such as a cross compiler for CloudABI. The reason for
this is that it makes more sense to upstream those packages to the
package collection of the respective operating system. They have the
infrastructure to package these tools for a variety of architectures and
versions of the operating system.

An advantage of shipping no native executables is that these packages
can be installed and used on any operating system. This repository
contains code to create native packages for a variety of operating
systems. This means that there is no special package manager for
CloudABI. You can simply use your operating system's package manager
that you're familiar with to install and manage CloudABI libraries.

## Accessing the CloudABI Ports Collection

Nuxi provides pre-built packages for a variety of operating systems that
are built periodically. The instructions below can be used to add the
repository for your operating system to the configuration of your
package manager.

### FreeBSD

FreeBSD's `pkg` can be configured to access the CloudABI repository by
running the following commands:

```sh
cd /etc/pkg
cat > CloudABI.conf << EOF
CloudABI: {
  url: https://nuxi.nl/distfiles/cloudabi-ports/freebsd
  signature_type: pubkey
  pubkey: /etc/pkg/CloudABI.key
}
EOF
cat > CloudABI.key << EOF
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7WeFa5CRgGzaJjsMuc4g
sBmBN54eazb7W97TC7jhZUMdtx+MguAomC0ducBPbuZtW1UQkIRY6FaVvMNOV/iE
/7k/Nlf8Et/JdHpS6EwFhYL4RB3AH1hM5TASvljZupBJQlVZ0bjsrkLrwTqHvj7X
BkqKEiJ5hNp/qOS2waCxuvqN1v4pU2Goyaf0xuRa9kCmJtSviiKXIFb4B8RYtMvd
hScf6H2bt0pqXGK0TvLbwESPv0Ez2jc3yqJ4rSx4oq5r/aXEd4lZZKYZkq44hNsa
ZdP5tV/tJLnDMof87iduXVme8WqmKgmXrMYwDU1UBriFpEQOVz/59JlyvCmlWZtm
7wIDAQAB
-----END PUBLIC KEY-----
EOF
pkg update
```

All packages are named `<arch>-<name>` and install their files under
`/usr/local/<arch>`. The
[standard C++ runtime](https://github.com/NuxiNL/cloudabi-ports/blob/master/packages/c%2B%2B-runtime/BUILD)
can be installed by running the following command:

```sh
pkg install x86_64-unknown-cloudabi-c++-runtime-1.0
```

A cross compiler for CloudABI can be obtained by installing FreeBSD's
`devel/cloudabi-clang` package.
