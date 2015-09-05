#!/bin/sh

set -e

find . -name '*.py' -o -name BUILD | while read file; do
  autopep8 --aggressive --aggressive --aggressive --in-place "$file"
done
