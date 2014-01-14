#!/bin/bash

if [[ -z $(git status | grep 'nothing to commit')  ]]; then
    echo "Commit first! Abort."
    exit 0
fi

export LANG=en; make clean; make html
rm -rf /tmp/output/
mv output/ /tmp/
git checkout gh-pages
\cp -ra /tmp/output/* ./
