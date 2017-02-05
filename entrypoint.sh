#!/bin/bash


# Add postgis to list of trusted repositories
echo 'Adding postgis to list of trusted repositories...'
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt trusty-pgdg main" >> /etc/apt/sources.list'
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -

echo 'Updating apt-get...'
apt-get update -y
apt-get upgrade -y

echo 'Installing PostgreSQL 9.5...'
apt-get install -y postgresql-9.5-postgis-2.2
echo 'Installing pgadmin3...'
apt-get install -y pgadmin3
echo 'Installing pgRouting 2.1...'
apt-get install -y postgresql-9.5-pgrouting
echo 'Installing Python for Postgres...'
apt-get install -y postgresql-plpython3-9.5

python manage.py migrate --noinput
gunicorn emergency_response_api.wsgi:application -b :8000
