#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn homelessAPI.wsgi:application -b :8000 --worker-class 'gevent' --workers 3

# python manage.py runserver 0.0.0.0:8000
