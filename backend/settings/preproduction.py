from .base import *

DEBUG = True

IMAGES_FOLDER = "preprod/images/"
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
SERVER_URL = '15.222.49.90'

SITE_URL = "{}".format(SERVER_URL)
SITE_URL_ROOT = "http://{}".format(SITE_URL)

BACKEND_URL = "{}:8000".format(SERVER_URL)
BACKEND_URL_ROOT = "http://{}".format(BACKEND_URL)

CORS_ORIGIN_WHITELIST = (
       SITE_URL_ROOT,
)

ENVIRONMENT = "preproduction"

EMAIL_HOST_USER = "elmahboub.preprod@gmail.com"
EMAIL_HOST_PASSWORD = "epassword.preprod"

DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': 'gdThVLGpVbAAAAAAAAAADU8bL3IZ2PKWJkrZvIX2qjfvj3bmEEXSUs4KH3oTUtqP',
}
