from .base import *

DEBUG = False

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ae_django_db",
        "USER": "ae_django_db",
        "PASSWORD": "ae_django_db",
        "HOST": "localhost",
        "PORT": "3306"
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://15.222.49.90',
)


SITE_URL = "15.222.49.90"
SITE_URL_ROOT = "http://{}".format(SITE_URL)

BACKEND_URL = "15.222.49.90:8000"
BACKEND_URL_ROOT = "http://{}".format(BACKEND_URL)

ENVIRONMENT = "production"
