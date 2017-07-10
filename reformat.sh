#!/bin/sh

set -e

git ls-files '*.py' '*/BUILD' | xargs -n1 -P8 yapf -i
