# -*- coding: utf-8 -*-


from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _


class SettingsDb(models.Model):
    class Meta:
        db_table = "settings_db"

    header_bg = models.ImageField(
        help_text=_("Header background image"),
        null=False,
        upload_to='images/settings_db/header'
    )
    logo = models.ImageField(help_text=_("Logo image"), null=False, upload_to='images/settings_db/header')
    site_name = models.CharField(_("Site name"), blank=False, max_length=255, null=False)

    home_page_title_1 = models.CharField(_("Title line 1"), blank=False, max_length=765, null=False)
    home_page_title_2 = models.CharField(_("Title line 2"), blank=True, max_length=765, null=True)

    home_page_left_column_title = models.CharField(_("Left column title"), blank=True, max_length=510, null=True)
    home_page_left_column_p_1 = models.TextField(_("Left column paragraph 1"), blank=True, null=True)
    home_page_left_column_p_2 = models.TextField(_("Left column paragraph 2"), blank=True, null=True)
    home_page_left_column_p_3 = models.TextField(_("Left column paragraph 3"), blank=True, null=True)

    home_page_right_column_title = models.CharField(_("Right column title"), blank=True, max_length=510, null=True)
    home_page_right_column_p_1 = models.TextField(_("Right column paragraph 1"), blank=True, null=True)
    home_page_right_column_p_2 = models.TextField(_("Right column paragraph 2"), blank=True, null=True)
    home_page_right_column_p_3 = models.TextField(_("Right column paragraph 3"), blank=True, null=True)

    home_page_row_1_title = models.CharField(_("Row 1 title"), blank=True, max_length=510, null=True)
    home_page_row_1_p_1 = models.TextField(_("Row 1 paragraph 1"), blank=True, null=True)
    home_page_row_1_p_2 = models.TextField(_("Row 1 paragraph 2"), blank=True, null=True)
    home_page_row_1_p_3 = models.TextField(_("Row 1 paragraph 3"), blank=True, null=True)

    home_page_row_2_title = models.CharField(_("Row 2 title"), blank=True, max_length=510, null=True)
    home_page_row_2_p_1 = models.TextField(_("Row 2 paragraph 1"), blank=True, null=True)
    home_page_row_2_p_2 = models.TextField(_("Row 2 paragraph 2"), blank=True, null=True)
    home_page_row_2_p_3 = models.TextField(_("Row 2 paragraph 3"), blank=True, null=True)

    def __str__(self):
        return "Settings databases"

    @classmethod
    def get_site_name(cls):
        try:
            return cls.objects.get().site_name
        except:
            return "Site name"

    @classmethod
    def get_header_settings(cls):
        try:
            return cls.objects.get().to_header_settings()
        except:
            return {
                "header_bg": "",
                "logo": "",
                "site_name": cls.get_site_name(),
            }

    def to_header_settings(self):
        return {
                "header_bg": settings.BACKEND_URL_ROOT + self.header_bg.url,
                "logo": settings.BACKEND_URL_ROOT + self.logo.url,
                "site_name": SettingsDb.get_site_name(),
        }

    @classmethod
    def get_home_page_data(cls):
        try:
            return cls.objects.get().to_home_page_data()
        except:
            return {
                "empty": True,
                "home_page_title_1": "",
                "home_page_title_2": "",
                "home_page_left_column_title": "",
                "home_page_left_column_p_1": "",
                "home_page_left_column_p_2": "",
                "home_page_left_column_p_3": "",
                "home_page_right_column_title": "",
                "home_page_right_column_p_1": "",
                "home_page_right_column_p_2": "",
                "home_page_right_column_p_3": "",
                "home_page_row_1_title": "",
                "home_page_row_1_p_1": "",
                "home_page_row_1_p_2": "",
                "home_page_row_1_p_3": "",
                "home_page_row_2_title": "",
                "home_page_row_2_p_1": "",
                "home_page_row_2_p_2": "",
                "home_page_row_2_p_3": "",
            }

    def to_home_page_data(self):
        return {
            "home_page_title_1": self.home_page_title_1,
            "home_page_title_2": self.home_page_title_2,
            "home_page_left_column_title": self.home_page_left_column_title,
            "home_page_left_column_p_1": self.home_page_left_column_p_1,
            "home_page_left_column_p_2": self.home_page_left_column_p_2,
            "home_page_left_column_p_3": self.home_page_left_column_p_3,
            "home_page_right_column_title": self.home_page_right_column_title,
            "home_page_right_column_p_1": self.home_page_right_column_p_1,
            "home_page_right_column_p_2": self.home_page_right_column_p_2,
            "home_page_right_column_p_3": self.home_page_right_column_p_3,
            "home_page_row_1_title": self.home_page_row_1_title,
            "home_page_row_1_p_1": self.home_page_row_1_p_1,
            "home_page_row_1_p_2": self.home_page_row_1_p_2,
            "home_page_row_1_p_3": self.home_page_row_1_p_3,
            "home_page_row_2_title": self.home_page_row_2_title,
            "home_page_row_2_p_1": self.home_page_row_2_p_1,
            "home_page_row_2_p_2": self.home_page_row_2_p_2,
            "home_page_row_2_p_3": self.home_page_row_2_p_3,
        }
