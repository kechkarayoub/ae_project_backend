from .base import *

DEBUG = False

IMAGES_FOLDER = "images/"
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
try:
    from .prod_conf import SERVER_URL
except:
    SERVER_URL = '91.234.194.87'

SITE_URL = "{}".format(SERVER_URL)
SITE_URL_ROOT = "http://{}".format(SITE_URL)

BACKEND_URL = "{}:8000".format(SERVER_URL)
BACKEND_URL_ROOT = "http://{}".format(BACKEND_URL)

CORS_ORIGIN_WHITELIST = (
       SITE_URL_ROOT,
)

ENVIRONMENT = "production"

EMAIL_HOST_USER = "elmahboubi.com@gmail.com"
EMAIL_HOST_PASSWORD = "epassword.com"

DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': 'BjiK4PwJO8AAAAAAAAAAFksZ5TCdI4CkWcT1uydZhGDTZNmKHbIYPWmwCN92Sb-Y',
}


MIGRATION_MODULES = {}
