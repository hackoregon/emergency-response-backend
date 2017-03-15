
#! /bin/bash

# PURPOSE: used to test that the DRF app is running inside the Docker container
# Can be used in Travis build or on local developer machine

echo Running test_proj.sh...

docker-compose run --entrypoint="python manage.py test --keepdb"  emerresponse-service
