#!/bin/sh

set -e

git ls-files '*.py' '*/BUILD' | \
  xargs -n1 -P8 autopep8 --aggressive --aggressive --aggressive --in-place
