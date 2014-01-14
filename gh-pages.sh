#!/bin/bash

export LANG=en; make clean; make html
rm -rf /tmp/output/
mv output/ /tmp/
git checkout gh-pages
\cp -ra /tmp/output/* ./
