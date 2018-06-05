import pytest
import os
import emerresponseAPI
from . import project_config


@pytest.fixture(scope='session')
def django_db_setup():
    transportation_systems_2018.settings.DATABASES['default'] = {
        'ENGINE': project_config.AWS['ENGINE'],
        'NAME': project_config.AWS['NAME'],
        'HOST': project_config.AWS['HOST'],
        'PORT': 5432,
        'USER': project_config.AWS['USER'],
        'PASSWORD': project_config.AWS['PASSWORD']
    }
