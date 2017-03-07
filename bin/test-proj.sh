#! /bin/bash
source ./bin/env.sh
docker-compose run emergency-response-service python manage.py test
