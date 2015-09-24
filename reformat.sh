#!/bin/sh

set -e

find . -name '*.py' -o -name BUILD -print0 | \
  xargs -0 -n1 -P8 autopep8 --aggressive --aggressive --aggressive --in-place
