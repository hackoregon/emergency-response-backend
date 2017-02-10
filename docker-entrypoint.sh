#!/bin/bash
source /code/secrets.sh
source /code/env.sh

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn emergency_response_api.wsgi:application -b :8000
