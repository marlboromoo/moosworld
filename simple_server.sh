#!/bin/bash

cd ~/project/moosworld/; export LANG=en; make clean; make html; cd output/; python -m SimpleHTTPServer
