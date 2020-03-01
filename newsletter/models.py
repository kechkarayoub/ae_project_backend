# -*- coding: utf-8 -*-


from django.db import models
from django.utils.translation import ugettext as _


class Newsletter(models.Model):
    class Meta:
        db_table = "newsletter"

    email = models.EmailField(_("Email"), null=False, unique=True)
    first_name = models.CharField(_("Prénom"), blank=False, max_length=30)
    is_active = models.BooleanField(_("Est active"), default=True)
    last_name = models.CharField(_("Nom"), blank=False, max_length=30)
