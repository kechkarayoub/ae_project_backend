# -*- coding: utf-8 -*-
from backend import static_variables
from backend.utils import choices_format_to_tuple
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _


class Testimonial(models.Model):
    class Meta:
        db_table = "testimonial"

    city = models.CharField(
        _("City"),
        blank=False,
        choices=choices_format_to_tuple(static_variables.CANADIAN_CITIES),
        default='montreal',
        max_length=100,
        null=False
    )
    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    first_name = models.CharField(_("First name"), blank=False, max_length=30)
    image = models.ImageField(
        help_text=_("User's image."),
        null=True,
        upload_to=settings.IMAGES_FOLDER + 'testimonial/UsersImages'  # lien de l'image: /media/images/testimonial/UsersImages/*.*
    )
    initials_bg_color = models.CharField(_("Initials background color"), default="#ffffff", max_length=10)
    initials_color = models.CharField(_("Initials color"), default="#000000", max_length=10)
    last_name = models.CharField(_("Last name"), blank=False, max_length=30)
    testimonial = models.TextField(_("Testimonial"), blank=False, null=False)
