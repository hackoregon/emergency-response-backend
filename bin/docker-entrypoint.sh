#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn emerresponseAPI.wsgi:application -b :8000 -k 'gevent' --keep-alive 60
# gunicorn emerresponseAPI.wsgi:application -b :8000
# python manage.py runserver 0.0.0.0:8000
