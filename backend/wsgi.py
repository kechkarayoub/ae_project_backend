"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
try:
    from .active_settings import ACTIVE_SETTINGS
except:
    ACTIVE_SETTINGS = "backend.settings.production"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", ACTIVE_SETTINGS)

application = get_wsgi_application()
