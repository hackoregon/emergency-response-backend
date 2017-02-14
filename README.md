# emergency-response
Simulations, Models, and Visualizations of Portland Fire and Rescue data

## Docker:

This API is built user Docker containers for the api and database. The easiest option to run is with [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) installed. If you would like to run natively see these [steps](#native). Any development work should be made with Docker.

## To Setup:

To run the API for the first time:

  1. Create the env.sh and secrets.sh files from templates:

        $ mv ./env-template.sh ./env.sh

        #! /bin/bash
        # Setup Project Specfics - Environment
        # Do not upload to github.  Make sure env.sh is in .gitignore
        # These will need to match your database settings postgres.
        export DB_NAME=<YOUR_DB>
        export DB_HOST=<YOUR_HOST>
        export DB_PORT=<YOUR_PORT>

        # For Hack Oregon:

        export DB_NAME=fire
        export DB_HOST=db
        export DB_PORT=5432

        $ mv ./secrets-template.sh ./secrets.sh

        #! /bin/bash
        # Setup Project Specfics - Secrets
        # Do not upload to github.  Make sure secrets.sh is in .gitignore
        # These will need to match your database settings in postgres.
        export DB_USER=<YOUR_USER_NAME>
        export DB_USER_PASS=<YOUR_DB_PASSWORD>

        # contact team member for login info for the docker container or build it from source [here](https://github.com/BrianHGrant/hacko-er-postgis-docker) to run locally with user created username/password

  2. cd into the root folder of this repo and run:  

        $ docker-compose up

      * You will most likely see an error during this process about the db refusing connections, this is do to boot order, and can be ignored.
  3. Allow process to run, will take a few minutes the first time as it needs to build the fresh image.

  4. Access the api at:

        $ http://localhost:8000/<endpoint>



## API Info:

    ## to view admin page/browsable endpoints

    ## open your browser in host machine

    ## for admin:

    $ http://localhost:8000/admin
    ## login using superuser info

    ## for endpoints preview:

    $ http://localhost:8000/<endpoint>

    ## ie:

    $ http://localhost:8000/agencies

## Existing API endpoints

<<<<<<< HEAD
    "agencies": "http://localhost:8000/agencies/",  
    "alarmlevels": "http://localhost:8000/alarmlevels/",  
    "censustracts": "http://localhost:8000/censustracts/",  
    "fireblocks": "http://localhost:8000/fireblocks/",  
    "typenaturecodes": "http://localhost:8000/typenaturecodes/",  
    "stations": "http://localhost:8000/stations/",  
    "firestations": "http://localhost:8000/firestations/",  
    "fmas": "http://localhost:8000/fmas/",  
    "mutualaid": "http://localhost:8000/mutualaid/",  
    "responderunits": "http://localhost:8000/responderunits/",  
    "incsitfoundclass": "http://localhost:8000/incsitfoundclass/",  
    "incsitfoundsub": "http://localhost:8000/incsitfoundsub/",  
    "incsitfound": "http://localhost:8000/incsitfound/",   
    "incidents": "http://localhost:8000/incidents/"  

## Pagination

    Pagination currently set to 10
    ## To select page:
    'http://localhost:4546/<endpoint>?page=NUM'


## Native

Provided the correct dependencies and versions are installed one should be able to run api outside of Docker.  

To Run:

  1. You will still need to download and save the dumpfile as directed.
  2. Setup the database, user, and import the data. Commands should be similar to above, removing docker syntax and using your postgres admin account:  

  ie:  

      $ createuser eruser --username=<YOURNAME>  
      $ createdb fire --username=<YOURNAME>  
      $ psql --username=<YOURNAME> fire < postgresql/data/fire_db_2010  

      * You will get some errors unless you have a user named postgres. This should not effect the usability of the api.  

  3. Alter /emergency_response_api/emergency_response_api/settings.py to match you postgres settings

  4. Make sure to migrate the database:

        $ python manage.py migrate  

  5. Run the server:

        $ gunicorn emergency_response_api.wsgi:application -b :8000  
