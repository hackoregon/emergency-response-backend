#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn emerresponseAPI.wsgi:application -b :8000 -k 'gevent' -w 5 --keep-alive 60 --log-level debug --access-logformat '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' --log-config logging.conf
# gunicorn emerresponseAPI.wsgi:application -b :8000
# python manage.py runserver 0.0.0.0:8000
