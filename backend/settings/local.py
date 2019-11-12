from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
       'http://localhost:3000',
)


SITE_URL = "localhost:3000"
SITE_URL_ROOT = "http://{}".format(SITE_URL)

BACKEND_URL = "localhost:5000"
BACKEND_URL_ROOT = "http://{}".format(BACKEND_URL)
