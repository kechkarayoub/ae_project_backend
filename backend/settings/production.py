from .base import *

DEBUG = False

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "full_app_db",
        "USER": "root",
        "PASSWORD": "full_app_pws",
        "HOST": "127.0.0.0",
        "PORT": "3306"
    }
}


CORS_ORIGIN_WHITELIST = (
       'localhost',
)