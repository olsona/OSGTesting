#!/bin/bash

cd $(dirname "$0")
dstring=$(date +%Y.%m.%d)
if [ ! -d "out/IO.${dstring}" ]
then
    mkdir "out/IO.${dstring}"
fi
python custom.py -r resources -o custom.sub
condor_submit custom.sub