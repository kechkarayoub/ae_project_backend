from .base import *

DEBUG = True

IMAGES_FOLDER = "dev/images/"
CATALOGS_FOLDER = "dev/catalogs/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SERVER_URL = 'localhost'

SITE_URL = "{}:3000".format(SERVER_URL)
SITE_URL_ROOT = "http://{}".format(SITE_URL)

BACKEND_URL = "{}:5000".format(SERVER_URL)
BACKEND_URL_ROOT = "http://{}".format(BACKEND_URL)

CORS_ORIGIN_WHITELIST = (
       SITE_URL_ROOT,
)

ENVIRONMENT = "development"

EMAIL_HOST_USER = "buildingssite2019@gmail.com"
EMAIL_HOST_PASSWORD = "building2019"

try:
    from .environement import DROPBOX_ACCESS_TOKEN
except:
    DROPBOX_ACCESS_TOKEN = ""
DBBACKUP_STORAGE_OPTIONS = {
    'oauth2_access_token': DROPBOX_ACCESS_TOKEN,
}

# MIGRATION_MODULES = dict([(app, 'migrations') for app in INSTALLED_APPS])

LOGGING = {}