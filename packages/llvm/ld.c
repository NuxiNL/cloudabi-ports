// Copyright (c) 2015 Nuxi, https://nuxi.nl/
//
// This file is distributed under a 2-clause BSD license.
// See the LICENSE file for details.

// ld - wrapper around LLD
//
// LLVM's new linker, LLD, can emulate multiple command line argument
// schemes (Windows, GNU, Darwin). The "-flavor" flag has to be
// specified to pick the dialect that should be used.
//
// This tool implements a simple wrapper around LLD, calling it with
// "-flavor gnu". That way we have a drop-in replacement for the GNU
// linker, normally provided by Binutils.

#include <stdio.h>
#include <unistd.h>

extern char **environ;

int main(int argc, char **argv) {
  // Prepare arguments for LLD.
  char *new_argv[argc + 3];
  new_argv[0] = (char *)PATH_LLD;
  new_argv[1] = (char *)"-flavor";
  new_argv[2] = (char *)"gnu";
  for (int i = 1; i <= argc; ++i)
    new_argv[i + 2] = argv[i];

  // Execute LLD.
  execve(PATH_LLD, new_argv, environ);
  perror("Failed to execute " PATH_LLD);
  return 127;
}
