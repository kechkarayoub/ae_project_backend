from .base import *

DEBUG = False

IMAGES_FOLDER = "images/"
CATALOGS_FOLDER = "catalogs/"
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
    SERVER_URL = 'www.elmahboubi.com'

SITE_URL = "{}".format(SERVER_URL)
SITE_URL_ROOT = "http://{}".format(SITE_URL)

BACKEND_URL = "{}:81".format(SERVER_URL)
BACKEND_URL_ROOT = "http://{}".format(BACKEND_URL)

CORS_ORIGIN_WHITELIST = (
       SITE_URL_ROOT,
)

ENVIRONMENT = "production"

EMAIL_HOST_USER = "elmahboubi.com@gmail.com"
EMAIL_HOST_PASSWORD = "epassword.com"
try:
    from .environement import DROPBOX_ACCESS_TOKEN
except:
    DROPBOX_ACCESS_TOKEN = ""
DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': DROPBOX_ACCESS_TOKEN,
}


MIGRATION_MODULES = {}
