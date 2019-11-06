from .base import *

DEBUG = False

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "full_app_db",
        "USER": "root",
        "PASSWORD": "full_app_pwd",
        "HOST": "",
        "PORT": ""
    }
}


CORS_ORIGIN_WHITELIST = (
       'http://ec2-35-183-204-35.ca-central-1.compute.amazonaws.com',
)