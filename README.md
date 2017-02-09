# emergency-response
Simulations, Models, and Visualizations of Portland Fire and Rescue data

## _IMPORTANT_

Before running, you must download the [fire_db_2010](https://drive.google.com/file/d/0B7k-dMOX1R5WOWpTZDdhMFBMUW8/view?usp=sharing) database file from the Hack Oregon Emergency Response shared drive.  

Save it to postgresql/data/ (will need to create folder) within this repo.

## DB Info:
to log into the DB use:

DB name: fire

username: eruser

password: fire


_BUT_ I set it up so you don't have to enter the password, just hit 'ok' if you are asked for a password in pgadmin.


## To Setup:

To run the API for the first time:

  1. Save the database file as discussed above.
  2. cd into the root folder of this repo and run:  
      $ docker-compose up
  3. Allow process to run, will take a few minutes the first time as it needs to build the fresh image.
  4. When completed you most likely will be confronted with an error about unable to find or connect to database.
  5. CTRL-C to stop the docker container.
  6. To configure postgres user and database and load data run the following commands in order:  

        ## this command will create the eruser  

        $ docker exec -i erapiv2_db_1 createuser eruser --username=postgres  

        ## this will create the fire database

        $ docker exec -i erapiv2_db_1 createdb fire --username=postgres


        ## this will load the data from the dumpfile  

        $ docker exec -i erapiv2_db_1 psql --username=postgres fire < postgresql/data/fire_db_2010  

  7. Run docker-compose up again to start api.

  8. Access the api at:

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

    '/incidents' pagination currently set to 10
    ## To select page:
    'http://localhost:4546/incidents?page=NUM'
