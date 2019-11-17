# -*- coding: utf-8 -*-
from backend import static_variables
from backend.utils import choices_format_to_tuple
from django.db import models
from django.utils.translation import ugettext as _


class Funding(models.Model):
    class Meta:
        db_table = "funding"

    city = models.CharField(
        _("City"),
        blank=False,
        choices=choices_format_to_tuple(static_variables.CANADIAN_CITIES),
        default='montreal',
        max_length=100,
        null=False
    )
    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    description = models.TextField(_("Description"), blank=False, null=False)
    first_name = models.CharField(_("First name"), blank=False, max_length=30)
    image = models.ImageField(
        help_text=_("User's image."),
        null=True,
        upload_to='images/funding/UsersImages'  # lien de l'image: /media/images/funding/UsersImages/*.*
    )
    initials_bg_color = models.CharField(_("Initials background color"), default="#ffffff", max_length=10)
    initials_color = models.CharField(_("Initials color"), default="#000000", max_length=10)
    last_name = models.CharField(_("Last name"), blank=False, max_length=30)
