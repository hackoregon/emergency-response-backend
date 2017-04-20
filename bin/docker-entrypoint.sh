#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh

python manage.py collectstatic --noinput
if [ "$DEBUG" == 'True' ]; then
  python manage.py runserver 0.0.0.0:8000
else
  gunicorn emerresponseAPI.wsgi:application -c gunicorn_config.py
fi
