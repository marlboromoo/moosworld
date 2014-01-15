#!/bin/bash

cd $(dirname $0); export LANG=en; make clean; make html; cd output/; python -m SimpleHTTPServer
