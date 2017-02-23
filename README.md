# emergency-response
This repo represents the backend development work for the Emeregency Response Team of Hack Oregon 2016-17 Project Season.

## Docker:

This API is built user Docker containers for the api and database. The easiest option to run is with [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/) installed. If you would like to run natively see these [steps](#native). Any development work should be made with Docker.

## To Setup:

To run the API for the first time:

  1. In the /emergency_response_api folder create a file project_config.py. This file is in the .gitignore so will not be committed with repo:

        AWS = {
                'ENGINE': 'django.contrib.gis.db.backends.postgis',
                'NAME': '<YOUR_AWS_DB_NAME>',
                'HOST': '<YOUR_AWS_DB_NAME>',
                'USER': '<YOUR_AWS_DB_NAME>',
                'PASSWORD': '<YOUR_AWS_DB_NAME>',
              }

        DJANGO_SECRET = <YOUR_DJANGO_SECRET>

  2. From project root run:  

        $ docker-compose up  

  Allow process to run, can take 20-30 minutes the first time as it needs to build the fresh image and install the geospatial libraries.

  3. Access the api at:

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

  1. Create the project_config.py file as instructed in the Docker settings.

  2. Run the server:

        $ gunicorn emergency_response_api.wsgi:application -b :8000  
