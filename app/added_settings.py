# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
I18N_ACTIVE = True

IS_MAPS_ACTIVE = True

SITE_NAME = "Site name"

SITE_URL = "localhost:3000"
SITE_URL_ROOT = "http://{}".format(SITE_URL)

BACKEND_URL = "localhost:5000"
BACKEND_URL_ROOT = "http://{}".format(BACKEND_URL)

ADMIN_EMAIL = "kechkarayoub@gmail.com"
REALTOR_DATA = {
    "full_name": "ELMAHBOUBI Abdjalil",
    "agency_name": "Agency Name",
    "address": _("address"),
    "email": ADMIN_EMAIL,
    "tel": "xxxxxxxxxx",
    "fax": "xxxxxxxxxx",
    "position": {
        "gps_latitude": 45.50866990,
        "gps_longitude": -73.55399250,
    }
}
