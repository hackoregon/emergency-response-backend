#!/bin/bash

export PATH=$PATH:~/.local/bin
./bin/getconfig.sh

python manage.py collectstatic --noinput
if [ "$DEBUG" == 'True' ]; then
  NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program python manage.py runserver 0.0.0.0:8000
else
  NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn emerresponseAPI.wsgi:application -c gunicorn_config.py
  # gunicorn emerresponseAPI.wsgi:application -b :8000 -k 'gevent' --access-logfile - --access-logformat '%(h)s %(t)s %(m)s %(U)s %(q)s %(H)s %(s)s %(B)s %(f)s %(a)s %(L)s'
fi
