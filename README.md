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

## Important:

This project was setup in a single database environment. Development, testing, and production have been connecting to same database. Prior to granting any write access to API, especially for testing ensure to change:
  1. The database credentials below will need to change to no longer override the "TEST_NAME" to 'fire', change other db creds as needed. It will then create a 'test_fire' database to run tests on. One will need to create method for loading test data.
   2. Ultimately to destroy the test db with each run you will remove the --keepdb argument from the test scripts.

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

        DJANGO_SECRET_KEY = <YOUR_DJANGO_SECRET>

  2. Create `env.sh` in the project ./bin folder. Make sure env.sh is in the .gitignore and .dockerignore (You will provide values if deploying to your own cluster. For the Hack Oregon project, consult the team.):

            export DOCKER_REPO=<NOT HERE>
            export DOCKER_IMAGE=<NOT HERE>
            export PROJ_SETTINGS_DIR=<NOT HERE>
            export DEPLOY_TARGET=<NOT HERE>
            export CONFIG_BUCKET=<NOT HERE>
            export AWS_ACCESS_KEY_ID=<NOT HERE>
            export AWS_SECRET_ACCESS_KEY=<NOT HERE>
            echo "##############################"
            echo  Your Local Project Environment
            echo "##############################"
            echo DOCKER_REPO: $DOCKER_REPO
            echo DOCKER_IMAGE: $DOCKER_IMAGE
            echo PROJ_SETTINGS_DIR: $PROJ_SETTINGS_DIR
            echo DEPLOY_TARGET: $DEPLOY_TARGET
            echo CONFIG_BUCKET: $CONFIG_BUCKET

  3. From project root run:  

        $ ./bin/build-proj.sh -l (flag is for local)

  Allow process to run, should build in a few minutes.

  4. Run the tests:
        $ ./bin/test-proj.sh -l

  5. To start project locally:

        $ ./bin/start-proj.sh -l

  6. Access the swagger docs at:

        $ http://localhost:8000/emergency

  7. Consult here for CI/CD info: https://github.com/hackoregon/backend-service-pattern

  8. For changes in the django code, stop the container and re-run the start-proj.sh command.

  9. For any changes to the docker image, additions to the pip packages (requirements.txt), or other non-code changes rerun the build-proj.sh command.

  10. If you are receiving a 'permission denied' notification on any of the shell commands, they may have lost the executable permission. run: $ chmod +x ./bin/*.* should correct the problem. You may choose to run command on individual files as well.


## API Info:

    ## to view admin page/browsable endpoints

    ## open your browser in host machine

    ## for endpoints preview:

    $ http://localhost:8000/emergency/<endpoint>

    ## ie:

    $ http://localhost:8000/emergency/agencies


## Pagination

    Pagination currently set to 50
    ## To select page:
    'http://localhost:4546/<endpoint>?page=NUM'


## Thank You:

Thanks to all the members of the Hack Oregon Team. This repo represents the work of many volunteers including the Hack Oregon 2017 Emergency Response and DevOps teams.
