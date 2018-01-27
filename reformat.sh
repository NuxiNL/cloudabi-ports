#!/bin/sh

set -e

mypy --strict *.py src/*.py
git ls-files '*.py' '*/BUILD' | xargs -n1 -P8 yapf -i
