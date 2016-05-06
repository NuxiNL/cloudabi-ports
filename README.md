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

Nuxi provides prebuilt packages for a variety of operating systems that
are updated periodically. Please refer to [Nuxi's website](https://nuxi.nl/)
for instructions on how to access these prebuilt packages on your
operating system.

## Support

### Public support

The
[cloudabi-devel@googlegroups.com](mailto:cloudabi-devel@googlegroups.com)
mailing list is used to discuss the development of CloudABI. It is
possible to sign up for this mailing list and browse its archive on
[Google Groups](https://groups.google.com/forum/#!forum/cloudabi-devel).

An IRC channel called `#cloudabi` exists on EFnet.

Bugs and pull requests can be submitted through
[GitHub](https://github.com/NuxiNL/cloudabi-ports).

### Commercial support

CloudABI has been developed by [Nuxi](https://nuxi.nl/), an IT company
based in the lovely city of
['s-Hertogenbosch, the Netherlands](http://en.wikipedia.org/wiki/%27s-Hertogenbosch).
Are you interested in receiving commercial support on CloudABI or any of
its components? Be sure to get in touch with us at info@nuxi.nl.
