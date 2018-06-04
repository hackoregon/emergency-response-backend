# 2017-2018 Migration Guide

These are the steps taken to migrate a 2017 Hack Oregon project based off backend service pattern to 2018 examplar:

1. Clone the 2017 project and 2018 examplar locally
2. Create a new branch
3. If you already have this project on the computer, you may already have some of the config files with variables saved on your computer. Look in the repo for the following files, and save into another location for the moment so that they are not deleted in the updating process:
  * any `env.sh` or sample `env.sh` files
  * any `project_config.py` files
  * anything else that seems to be an env file ie: `.env`

3. Remove the bin folder completely, ie: `rm -rf ./bin`
4. Copy the bin folder over completely from the examplar into the project, to replace the folder you just removed.
5. Update the name of the api service in the the `production-docker-compose` ie: `emergency-service`
5. Remove the following files as well:
  * Dockerfile
  * local-docker-compose.yml
  * travis-docker-compose.yml
  * .travis.yml
  * .gitignore (we are going to copy over in the next step)
  * .dockerignore (same as above)

6. Copy the following files/folders over from the examplar:
  * .gitignore
  * .dockerignore
  * env.sample
  * development-docker-compose.yml
  * production-docker-compose.yml
  * DOCKERFILE.api.development
  * DOCKERFILE.api.production
  * DOCKERFILE.db.development
  * gunicorn.py
  * Backups
  * postgis-scripts

7. Now those were the easy parts. Next we need to meld the requirements.txt into the updated setup. Generally we should be using similar packages, just updating version numbers, and separating into the environments where necessary. You should have four files:

  * common.txt - used in both development and production (this will including testing).
  * production.txt - any packages only used in production
  * development.txt - any packages only used in development
  * geodjango.txt - additional file to contain any geodjango Dependencies.

8. Next will be updating the setup and use of the environmental variables and secrets. By copying the bin and other files over directly most of the places which refer to the env vars have already been updated. We will have to look at the `settings.py` file, but will get there shortly. For now you will want to begin by comparing the env variables that were set last year and translating these to this years pattern.

This will be a bit difficult as env vars were set in multiple locations and had no standardization across projects. Let's try to cut out this pattern, and work with DevOps to update as necessary. Here are some places to look:

* Any `env.sh` or `sample env.sh`
* a `project_config.py` file or sample one (should be in the same folder of the settings.py, if you already have the project on your machine)
* the Travis settings for the project, if you have access
* who knows? maybe the project has a README
* The 2017 backend service repo also contains some values, though some of these maybe needing updates.

So using the info from these sources, you should have what you need to fill in the env values.

Go ahead and cp the env.sample over to the .env: `cp env.sample .env`.

9. For our last feet of heroics we'll update the Django app itself.

10. First go into the main project folder and find the `wsgi.py`. Compare this to the one in the examplar. Some projects made changes within this file to run whitenoise or monkeypatch. These updates are no longer necessary. Generally we should err on the side of using the the standardized version of this file. If you are unsure, make sure to make a backup of this

11. Next it's time to tackle the `settings.py`. This one you may need to walk through and compare line by line. Here's a general idea of what needs to update:

12. We are removing the `project_config.py` pattern of importing environmental variables and instead treating directly as OS variables. This is accomplished through 3 different processes depending on the environment:

* Locally through the `.env`
* Through configuration in the Travis UI in the CI/CD chain
* Through AWS parameter store in EC2

In the end though the Django app sees these are the same way. So in the settings.py file, you will want to remove this line:

```
from . import project_config
```

Make sure instead that you are importing OS:

```
import os
```

Then update lines which refer to the `project_config` to look for os environs instead. For example:

```
SECRET_KEY = project_config.DJANGO_SECRET_KEY
```

Becomes:

```
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
```

You will want to be careful to note that os variables are all passed as strings to the Django app. You may also come across variables that are not in the current env.sample. Again we would generally err on the side of the pattern in our current examplar but if you are unsure of what to do reach out for assistance from DevOps or #api in our slack.

13. Make note of how we are handling the `DEBUG` variable.

14. Update installed apps as needed. If you have a reference to whitenoise in this section remove it from installed apps. The way to integrate this has changed.

15. Update the database settings. This will include:

  * No longer using `project_config.py` and instead the os variables
  * updating the db ENGINE
  * providing the two different drivers depending on the debug flag.

For example, replacing:

```
DATABASES = {
    'default': {
        'ENGINE': project_config.AWS['ENGINE'],
        'NAME': project_config.AWS['NAME'],
        'HOST': project_config.AWS['HOST'],
        'PORT': 5432,
        'USER': project_config.AWS['USER'],
        'PASSWORD': project_config.AWS['PASSWORD'],
    },
```

With:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    }
}

if DEBUG == False:

    DATABASES = {
        'default': {
            'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'NAME': os.environ.get('POSTGRES_NAME'),
            'USER': os.environ.get('POSTGRES_USER'),
            'HOST': os.environ.get('POSTGRES_HOST'),
            'PORT': os.environ.get('POSTGRES_PORT'),
            'CONN_MAX_AGE': 0,
            'OPTIONS': {
                'MAX_CONNS': 20
            }
        }
    }
```

16. Take a final look through and note any differences you think might cause issues.

17. Update your root urls.py file. We are trying to put swagger at the root. Something like this should work:

```
from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter


from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hack Oregon 2017 Emergency Response APIs')

urlpatterns = [
    url(r'^emergency/$', schema_view),
    url(r'emergency/api/', include('data.urls')),
]
```

18. Try to build and run and triage any issues that come up.

19. Update the testing schema (Separate article)
