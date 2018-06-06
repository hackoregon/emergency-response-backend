import pytest
import os
import emerresponseAPI

@pytest.fixture(scope='session')
def django_db_setup():
    emerresponseAPI.settings.DATABASES['default'] = {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    }
