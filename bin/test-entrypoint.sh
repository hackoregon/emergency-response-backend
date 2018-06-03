#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
echo "DEBUG: " $DEBUG

pytest
