# -*- coding: utf-8 -*-


from django.db import models
from backend import static_variables
from backend.utils import choices_format_to_tuple
import os
import datetime
from django.utils.translation import ugettext as _


class Item(models.Model):
    class Meta:
        db_table = "item"

    address = models.CharField(_("Address"), blank=False, max_length=510, null=False)
    bathrooms_number = models.CharField(
        _("Bathrooms number"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.BATHROOMS_NUMBER),
        default='',
        max_length=10
    )
    bedrooms_number = models.CharField(
        _("Bedrooms number"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.BEDROOMS_NUMBER),
        default='',
        max_length=10
    )
    building_type = models.CharField(
        _("Building type"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.BUILDINGS_TYPES),
        default='',
        max_length=50
    )
    city = models.CharField(
        _("City"),
        blank=False,
        choices=choices_format_to_tuple(static_variables.CANADIAN_CITIES),
        default='montreal',
        max_length=100,
        null=False
    )
    construction_age = models.CharField(
        _("Construction age"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.CONSTRUCTION_AGE),
        default='',
        max_length=50
    )
    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    description = models.TextField(_("Description"), blank=False, null=False)
    gps_latitude = models.FloatField(_("Latitude"), blank=True, default=46.813878, null=True)
    gps_longitude = models.FloatField(_("Longitude"), blank=True, default=-71.207981, null=True)
    has_dining_room = models.BooleanField(_("Dining room"), default=False)
    has_fireplace = models.BooleanField(_("Fireplace"), default=False)
    has_garage = models.BooleanField(_("Garage"), default=False)
    has_garden = models.BooleanField(_("Garden"), default=False)
    has_swimming_pool = models.BooleanField(_("Swimming pool"), default=False)
    image_map = models.ImageField(
        help_text=_("Item's map's image."),
        null=True, blank=True,
        upload_to='images/item/itemsImages'  # lien de l'image: /media/item/images/itemsImages/*.*
    )
    item_id = models.CharField(_("Id"), max_length=255, primary_key=True, unique=True)
    is_active = models.BooleanField(_("Is active"), default=True)
    label = models.CharField(_("Label"), blank=False, max_length=255, null=False)
    lot_size = models.PositiveIntegerField(_("Lot size(m²)"), default=0)
    price = models.PositiveIntegerField(_("Price"), default=0)
    property_type = models.CharField(
        _("Property type"),
        blank=False,
        choices=choices_format_to_tuple(static_variables.PROPERTIES_TYPES),
        default='',
        max_length=50,
        null=False
    )
    short_description = models.CharField(_("Short description"), max_length=255, null=False, blank=False)
    status = models.CharField(
        _("Status"),
        choices=choices_format_to_tuple(static_variables.ITEMS_STATUS),
        default='for_sale',
        max_length=50
    )
    with_map = models.BooleanField(_("With map"), default=False)

    def __str__(self):
        return self.item_id

    @property
    def is_new(self):
        delta = datetime.datetime.now().date() - self.createdAt.date()
        return delta.days < 8


class ItemImage(models.Model):
    class Meta:
        db_table = "itemimage"

    image = models.ImageField(
        help_text=_("Item's image."),
        upload_to='images/item/itemsImages'  # lien de l'image: /media/item/images/itemsImages/*.*
    )
    item = models.ForeignKey(
        Item,
        db_index=True,
        help_text=_("Image's item."),
        on_delete=models.CASCADE,
        related_name="images"
    )

    def __str__(self):
        return str(self.image)[str(self.image).rfind('/') + 1:]

    @property
    def image_filename(self):
        return os.path.basename(self.image.name)
