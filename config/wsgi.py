"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

if 'runserver' in sys.argv:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings-debug')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings-heroku') 

application = get_wsgi_application()
