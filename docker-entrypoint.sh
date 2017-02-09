#!/bin/bash

python manage.py migrate --noinput
gunicorn emergency_response_api.wsgi:application -b :8000
