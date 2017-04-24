#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
echo "Hello, testing"
echo $DOCKER_IMAGE
echo $DEBUG
python manage.py test --keepdb
