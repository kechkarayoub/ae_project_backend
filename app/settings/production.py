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
