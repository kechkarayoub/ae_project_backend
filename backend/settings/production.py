from .base import *

DEBUG = False

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ae_django_db",
        "USER": "ae_django_db",
        "PASSWORD": "ae_django_db",
        "HOST": "ae-django-db.cpg8jmousblr.ca-central-1.rds.amazonaws.com",
        "PORT": "3306"
    }
}

CORS_ORIGIN_WHITELIST = (
       'http://35.183.147.63',
)


CORS_ORIGIN_WHITELIST = (
       'http://35.183.147.63',
)


SITE_URL = "http://35.183.147.63"
SITE_URL_ROOT = "http://{}".format(SITE_URL)

BACKEND_URL = "http://35.182.105.225"
BACKEND_URL_ROOT = "http://{}".format(BACKEND_URL)
