from .base import *


IMAGES_FOLDER = "dev/images/"

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
