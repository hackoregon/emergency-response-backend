#!/usr/bin/env python
import os
import sys

# from gevent import monkey;
# from psycogreen.gevent import patch_psycopg
# monkey.patch_all()
# patch_psycopg()

if sys.argv == 'runserver':
    os.environ["ENVIRONMENT"] = 'development' 

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emerresponseAPI.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
