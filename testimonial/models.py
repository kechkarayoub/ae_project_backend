# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _


class Testimonial(models.Model):
    class Meta:
        db_table = "testimonial"

    city = models.CharField(_("City label"), default='', max_length=100)
    city_val = models.CharField(_("City"), blank=True, default='', max_length=100)
    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    first_name = models.CharField(_("First name"), blank=False, max_length=30)
    initials_bg_color = models.CharField(_("Initials background color"), default="#ffffff", max_length=10)
    initials_color = models.CharField(_("Initials color"), default="#000000", max_length=10)
    last_name = models.CharField(_("Last name"), blank=False, max_length=30)
    testimonial = models.TextField(_("Testimonial"), blank=False, null=False)
