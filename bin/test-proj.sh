#! /bin/bash
source ./env.sh
source ./secrets.sh
docker-compose run web python manage.py test
