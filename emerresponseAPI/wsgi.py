"""
WSGI config for project project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import sys
import os
if os.environ.get("ENVIRONMENT") != "development":
    from gevent import monkey;
    from psycogreen.gevent import patch_psycopg
    monkey.patch_all()
    patch_psycopg()
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emerresponseAPI.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
