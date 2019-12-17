# -*- coding: utf-8 -*-


from backend import static_variables
from backend.utils import choices_format_to_tuple
from django.db import models
from django.utils.translation import ugettext as _


class Contact(models.Model):
    class Meta:
        db_table = "contact"

    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    email = models.EmailField(_("Email"), null=False)
    first_name = models.CharField(_("First name"), blank=False, max_length=30)
    last_name = models.CharField(_("First name"), blank=False, max_length=30)
    message = models.TextField(_("Message"), blank=False, null=False)
    object = models.CharField(_("Subject"), blank=False, max_length=30)
    phone = models.CharField(_("Phone"), blank=True, default="", max_length=20)


class ContactBuy(models.Model):
    class Meta:
        db_table = "contact_buy"

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
        default='',
        blank=True,
        max_length=50,
        choices=choices_format_to_tuple(static_variables.BUILDINGS_TYPES))
    city = models.CharField(
        _("City"),
        choices=choices_format_to_tuple(static_variables.CANADIAN_CITIES),
        default='',
        max_length=100
    )
    construction_age = models.CharField(
        _("Construction age"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.CONSTRUCTION_AGE),
        default='',
        max_length=20
    )
    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    email = models.EmailField(_("Email"), null=False)
    first_name = models.CharField(_("First name"), blank=False, max_length=30)
    has_dining_room = models.BooleanField(_("Dining room"), default=False)
    has_fireplace = models.BooleanField(_("Fireplace"), default=False)
    has_garage = models.BooleanField(_("Garage"), default=False)
    has_garden = models.BooleanField(_("Garden"), default=False)
    has_swimming_pool = models.BooleanField(_("Swimming pool"), default=False)
    is_active = models.BooleanField(default=True)
    last_name = models.CharField(_("First name"), blank=False, max_length=30)
    lot_size_min = models.PositiveIntegerField(_("Property size min(m²)"), default=0,)
    lot_size_max = models.PositiveIntegerField(_("Property size max(m²)"), default=0,)
    occupation_date = models.DateField(_("Occupation date"), null=True)
    other_characteristics = models.TextField(_("Other characteristics"), blank=True, null=True)
    phone = models.CharField(_("Phone"), blank=True, default="", max_length=20)
    price_range = models.CharField(
        _("Price range"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.PRICES_RANGES),
        default='',
        max_length=50
    )
    property_type = models.CharField(
        _("Property type"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.PROPERTIES_TYPES),
        default='',
        max_length=50
    )
    status = models.CharField(
        _("Status"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.ITEMS_STATUS),
        default='for_sale',
        max_length=20
    )
