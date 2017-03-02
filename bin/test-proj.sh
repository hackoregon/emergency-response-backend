#! /bin/bash
source ./bin/env.sh
docker-compose run homeless-service python manage.py test
