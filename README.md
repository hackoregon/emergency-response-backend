# emergency-response
This repo represents the backend development work for the Emergency Response Team of Hack Oregon 2016-17 Project Season. The development and deployment chain is modeled on the pattern contained here:  

https://github.com/hackoregon/backend-service-pattern

## Dependencies

* Docker or Docker toolkit
* Database Read-Only Credentials (assumes AWS, otherwise updated settings.py and project_config.py accordingly, Contact Emergency Response Team)
* Travis-CI (not required for local dev)
* Cluster deployment keys  - Contact the DevOps team (not required for local dev)
* ECS Service Name - Contact the DevOps team (not required for local dev)

## Docker:

This API is built using [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) installed.

## To Setup:

To run the API for the first time:

  1. In the /emergency_response_api folder create a file project_config.py. Make sure env.sh is in the .gitignore and .dockerignore:

        AWS = {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': '<YOUR_AWS_DB_NAME>',
                'HOST': '<YOUR_AWS_DB_NAME>',
                'USER': '<YOUR_AWS_DB_NAME>',
                'PASSWORD': '<YOUR_AWS_DB_NAME>',
              }

        DJANGO_SECRET = <YOUR_DJANGO_SECRET>

  2. Create `env.sh` in the project ./bin folder. Make sure env.sh is in the .gitignore and .dockerignore:

            export DOCKER_REPO=<YOUR REPO>
            export DOCKER_IMAGE=<the name of your service>
            export DOCKER_USERNAME=<YOUR DOCKER Repository USER NAME>
            export DOCKER_PASSWORD=<YOUR DOCKER Repository PASSWORD>
            export ECS_CLUSTER=<THE NAME OF YOUR ECS CLUSTER>
            export ECS_SERVICE_NAME=<THE NAME OF THE SERVICE YOUR DEPLOYING TO>
            echo "##############################"
            echo  Your Local Project Environment
            echo "##############################"
            echo DOCKER_REPO: $DOCKER_REPO
            echo DOCKER_IMAGE: $DOCKER_IMAGE
            echo DOCKER_USERNAME: $DOCKER_USERNAME
            echo DOCKER_PASWORD: $DOCKER_PASSWORD
            echo ECS_CLUSTER: $ECS_CLUSTER
            echo ECS_SERVICE_NAME: $ECS_SERVICE_NAME


  3. From project root run:  

        $ ./bin/build-proj.sh  

  Allow process to run, can take 20-30 minutes the first time as it needs to build the fresh image and install the geospatial libraries.

  4. To start project locally:

        $ ./bin/start-proj.sh  

  5. Access the swagger docs at:

        $ http://localhost:8000/

  6. Consult here for CI/CD info: https://github.com/hackoregon/backend-service-pattern

  7. For changes in the django code, stop the container and re-run the start-proj.sh command.

  8. For any changes to the docker image, additions to the pip packages (requirements.txt), or other non-code changes rerun the build-proj.sh command.

  9. If you are receiving a 'permission denied' notification on any of the shell commands, they may have lost the executable permission. run: $ chmod +x ./bin/*.* should correct the problem. You may choose to run command on individual files as well.


## API Info:

    ## to view admin page/browsable endpoints

    ## open your browser in host machine

    ## for endpoints preview:

    $ http://localhost:8000/<endpoint>

    ## ie:

    $ http://localhost:8000/agencies


## Pagination

    Pagination currently set to 50
    ## To select page:
    'http://localhost:4546/<endpoint>?page=NUM'
