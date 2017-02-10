#!/bin/bash


source ./code/bin/secrets.sh
source ./code/bin/env.sh

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn emergency_response_api.wsgi:application -b :8000
