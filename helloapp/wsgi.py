"""
WSGI config for helloapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys


from django.core.wsgi import get_wsgi_application
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise



sys.path.append('/app/helloapp/settings')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "helloapp.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)


