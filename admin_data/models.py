# -*- coding: utf-8 -*-


from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


class AdminData(models.Model):
    class Meta:
        db_table = "admin_data"

    address = models.CharField(_("Address"), blank=False, max_length=510, null=False)
    agency_name = models.CharField(_("Agency name"), blank=False, max_length=255, null=False)
    email = models.CharField(_("Email"), blank=False, default="Jalil.elmahboubi@gmail.com", max_length=255, null=False)
    enable_map = models.BooleanField(_("Enable map"), default=True)
    fax = models.CharField(_("Fax"), blank=False, default="XXXXXXXXXX", max_length=255, null=False)
    full_name = models.CharField(_("Full name"), blank=False, default="ELMAHBOUBI Abdjalil", max_length=255, null=False)
    gps_latitude = models.FloatField(_("GPS Latitude"), blank=True, default=45.50866990, null=True)
    gps_longitude = models.FloatField(_("GPS Longitude"), blank=True, default=-73.55399250, null=True)
    image = models.ImageField(help_text=_("Admin's image"), null=False, upload_to='images/admin_data')
    tel = models.CharField(_("Telephone"), blank=False, default="XXXXXXXXXX", max_length=255, null=False)

    def __str__(self):
        return "Admin data"

    @classmethod
    def get_admin_email(cls):
        try:
            return cls.objects.get().email
        except:
            return "Jalil.elmahboubi@gmail.com"

    @classmethod
    def get_admin_data(cls):
        try:
            return cls.objects.get().to_dict()
        except:
            return {
                "full_name": "ELMAHBOUBI Jalil",
                "agency_name": "Agency Name",
                "address": _("address"),
                "email": cls.get_admin_email(),
                "image": "",
                "tel": "xxxxxxxxxx",
                "fax": "xxxxxxxxxx",
                "position": {
                    "gps_latitude": 45.50866990,
                    "gps_longitude": -73.55399250,
                }
            }

    def to_dict(self):
        res = {
            "address": self.address,
            "agency_name": self.agency_name,
            "email": self.email,
            "enable_map": self.address,
            "fax": self.fax,
            "full_name": self.full_name,
            "image": settings.BACKEND_URL_ROOT + self.image.url,
            "tel": self.tel
        }
        if self.enable_map:
            res["position"] = {
                "gps_latitude": self.gps_latitude,
                "gps_longitude": self.gps_longitude
            }
        return res