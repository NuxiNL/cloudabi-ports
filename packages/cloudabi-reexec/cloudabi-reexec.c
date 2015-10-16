// Copyright (c) 2015 Nuxi, https://nuxi.nl/
//
// This file is distrbuted under a 2-clause BSD license.
// See the LICENSE file for details.

// cloudabi-reexec - execute a program indirectly
//
// The cloudabi-reexec utility is used by cloudabi-run to execute the
// requested binary. It is invoked with a sequence containing the file
// descriptor of the program that needs to be executed and its argument
// data.
//
// The idea behind cloudabi-reexec is that by running a CloudABI
// executable already before executing the program, we already instruct
// the kernel to place the process in capabilities mode. Furthermore,
// the CloudABI program_exec() call prevents leaking file descriptors to
// the new process by accident.
//
// When the program is unable to start the target executable, it writes
// its error message to file descriptor 2, stderr. This is safe, as
// cloudabi-run also writes diagnostic messages to this file descriptor.

#include <sys/uio.h>

#include <argdata.h>
#include <program.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

static int fd = -1;

static bool iterate(const argdata_t *ad, void *thunk) {
  if (fd < 0) {
    // First element in sequence: a file descriptor of the executable.
    return argdata_get_fd(ad, &fd) == 0;
  } else {
    // Second element in sequence; arguments data for the executable.
    int error = program_exec(fd, ad);

    // Print error message without depending on stdio.
    static const char prefix[] = "Failed to start executable: ";
    struct iovec iov[3] = {
        {.iov_base = (char *)prefix, .iov_len = sizeof(prefix) - 1},
        {.iov_base = strerror(error), .iov_len = strlen(iov[1].iov_base)},
        {.iov_base = (char *)"\n", .iov_len = 1},
    };
    writev(2, iov, __arraycount(iov));
    _Exit(127);
  }
}

void program_main(const argdata_t *ad) {
  argdata_iterate_seq(ad, iterate, NULL);
  static const char message[] = "Failed to parse argument data\n";
  write(2, message, sizeof(message) - 1);
  _Exit(127);
}
