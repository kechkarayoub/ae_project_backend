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
       'ec2-35-183-37-3.ca-central-1.compute.amazonaws.com',
)