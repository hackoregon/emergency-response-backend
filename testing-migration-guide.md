# 2017-2018 Testing Migration Guide

This guide is intended to be a workflow to update from a testing schema used in 2017 to 2018's project season.

There are a few things that have happened:

* The test runner used by many teams `nose` is no longer maintained so we are deprecating its use.
* Many teams relyed on some sort of test db creation or loading of fixture data. This year we are assuming all projects are read only and will run against prod.

While updating from the 2017 to 2018 you may have already run into some dependency issues related to test packages and have begun this process. But this will assume you are starting from scratch.

1. Remove any references to `nose` or `nose_coverage` in the `settings.py` file

2. Also remove these packages from the requirements files.

3. Confirm you have these testing packages in the `common.txt`:

```
# Testing
pytest-django==3.2.1
tblib==1.3.2
```

4. Create a `pytest.ini` file at the project root (Replace `emerresponseAPI` with actual project name):

```
[pytest]
DJANGO_SETTINGS_MODULE = emerresponseAPI.settings
python_files = tests.py test_*.py *_tests.py
addopts = --reuse-db
```

5. Create a `confttest.py` file also at the project root (Again updating to project name as needed):

```
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

```

6. Remove any fixture files from the project and comment out all current tests.

7. Begin with a test on the root endpoint and confirm it passes:

```
from django.test import TestCase
from rest_framework.test import APIClient, RequestsClient

class RootTest(TestCase):
    """ Test for Crash model """

    def setUp(self):
        pass

class RootEndpointsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    def test_list_200_response(self):
        response = self.client.get('/emergency/')
        assert response.status_code == 200
```

8. Now go tests, confirming they pass one by one. You will need to do two things:

* Make sure nothing is attempting to write/create/destroy any data.
* Make sure the expected data results match those returned
