#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
echo $DEBUG
python manage.py test --keepdb
