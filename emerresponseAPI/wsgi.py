"""
WSGI config for project project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
try:
    from gevent import monkey
    monkey.patch_all()
except RuntimeError:
    pass

try:
    import psycogreen.gevent
    psycogreen.gevent.patch_psycopg()
except RuntimeError:
    pass

from whitenoise.django import DjangoWhiteNoise

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emerresponseAPI.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
