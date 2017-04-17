#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
# python manage.py makemigrations --noinput
# python manage.py migrate --noinput
# python manage.py collectstatic --noinput
gunicorn emerresponseAPI.wsgi:application -b :8000 -k 'gevent' --access-logfile - --access-logformat '%(h)s %(t)s "%(r)s" %(m)s “%(U)s” “%(q)s” %(H)s %(s)s %(B)s %(f)s %(a)s %(L)s'
# gunicorn emerresponseAPI.wsgi:application -b :8000
# python manage.py runserver 0.0.0.0:8000
