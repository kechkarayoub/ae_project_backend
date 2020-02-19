# -*- coding: utf-8 -*-


from backend import static_variables
from backend.utils import choices_format_to_tuple
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
import datetime
import os


class Item(models.Model):
    class Meta:
        db_table = "item"

    added_field_1_label = models.CharField(_("Added field 1 label"), blank=True, max_length=255, null=True)
    added_field_1_value = models.CharField(_("Added field 1 value"), blank=True, max_length=255, null=True)
    added_field_2_label = models.CharField(_("Added field 2 label"), blank=True, max_length=255, null=True)
    added_field_2_value = models.CharField(_("Added field 2 value"), blank=True, max_length=255, null=True)
    added_field_3_label = models.CharField(_("Added field 3 label"), blank=True, max_length=255, null=True)
    added_field_3_value = models.CharField(_("Added field 3 value"), blank=True, max_length=255, null=True)
    address = models.CharField(_("Address"), blank=False, max_length=510, null=False)
    annual_income = models.DecimalField(
        _("Annual incomes ($)"), blank=True, decimal_places=0, max_digits=9, null=True
    )
    apartments_number = models.PositiveIntegerField(_("Apartments number"), blank=True, null=True)
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
    ccd = models.DecimalField(
        _("Ccd (CCD)"), blank=True, decimal_places=2, max_digits=5, null=True
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
    cost_per_housing = models.DecimalField(
        _("Cost per housing (CPH) ($)"), blank=True, decimal_places=0, max_digits=9, null=True
    )
    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    description = models.TextField(_("Description"), blank=False, null=False)
    down_payment_required = models.DecimalField(
        _("Down payment required ($)"), blank=True, decimal_places=0, max_digits=9, null=True
    )
    economic_value = models.DecimalField(
        _("Economic value ($)"), blank=True, decimal_places=0, max_digits=9, null=True
    )
    gps_latitude = models.FloatField(_("Latitude"), blank=True, default=46.813878, null=True)
    gps_longitude = models.FloatField(_("Longitude"), blank=True, default=-71.207981, null=True)
    gross_revenue_multiplier = models.DecimalField(
        _("Gross revenue multiplier (GRM)"), blank=True, decimal_places=1, max_digits=4, null=True
    )
    has_dining_room = models.BooleanField(_("Dining room"), default=False)
    has_fireplace = models.BooleanField(_("Fireplace"), default=False)
    has_garage = models.BooleanField(_("Garage"), default=False)
    has_garden = models.BooleanField(_("Garden"), default=False)
    has_swimming_pool = models.BooleanField(_("Swimming pool"), default=False)
    housing_descriptions = models.CharField(_("Housing descriptions"), blank=True, max_length=1020, null=True)
    image_map = models.ImageField(
        help_text=_("Item's map's image."),
        null=True, blank=True,
        upload_to=settings.IMAGES_FOLDER + 'item/itemsImages'  # lien de l'image: /media/item/images/itemsImages/*.*
    )
    item_id = models.CharField(_("Id"), max_length=255, primary_key=True, unique=True)
    is_active = models.BooleanField(_("Is active"), default=True)
    label = models.CharField(_("Label"), blank=False, max_length=255, null=False)
    lot_size = models.PositiveIntegerField(_("Property size(m²)"), default=0)
    maximum_loan = models.DecimalField(
        _("Maximum loan (%)"), blank=True, decimal_places=2, max_digits=5, null=True
    )
    net_income_multiplier = models.DecimalField(
        _("Net income multiplier (NIM)"), blank=True, decimal_places=1, max_digits=4, null=True
    )
    overall_rate_update = models.DecimalField(
        _("Overall rate of update (ORU) (%)"), blank=True, decimal_places=1, max_digits=4, null=True
    )
    price = models.DecimalField(
        _("Price"), blank=False, decimal_places=0, default=0, max_digits=9, null=False
    )
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
        return self.label

    @property
    def is_new(self):
        delta = datetime.datetime.now().date() - self.createdAt.date()
        return delta.days < 8


class ItemImage(models.Model):
    class Meta:
        db_table = "itemimage"

    image = models.ImageField(
        help_text=_("Item's image."),
        upload_to=settings.IMAGES_FOLDER + 'item/itemsImages'  # lien de l'image: /media/item/images/itemsImages/*.*
    )
    item = models.ForeignKey(
        Item,
        db_index=True,
        help_text=_("Item's image."),
        on_delete=models.CASCADE,
        related_name="images"
    )

    def __str__(self):
        return str(self.image)[str(self.image).rfind('/') + 1:]

    @property
    def image_filename(self):
        return os.path.basename(self.image.name)
