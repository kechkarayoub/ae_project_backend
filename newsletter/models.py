# -*- coding: utf-8 -*-


from django.db import models
from django.utils.translation import ugettext as _


class Newsletter(models.Model):
    class Meta:
        db_table = "newsletter"

    email = models.EmailField(_("Email"), null=False, unique=True)
    first_name = models.CharField(_("First name"), blank=False, max_length=30)
    is_active = models.BooleanField(_("Is active"), default=True)
    last_name = models.CharField(_("First name"), blank=False, max_length=30)
