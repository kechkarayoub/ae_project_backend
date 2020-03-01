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

    added_field_1_label = models.CharField(_("Étiquette du 1er champ ajouté"), blank=True, max_length=255, null=True)
    added_field_1_value = models.CharField(_("Valeur du 1er champ ajouté"), blank=True, max_length=255, null=True)
    added_field_2_label = models.CharField(_("Étiquette du 2eme champ ajouté"), blank=True, max_length=255, null=True)
    added_field_2_value = models.CharField(_("Valeur du 1er champ ajouté"), blank=True, max_length=255, null=True)
    added_field_3_label = models.CharField(_("Étiquette du 3eme champ ajouté"), blank=True, max_length=255, null=True)
    added_field_3_value = models.CharField(_("Valeur du 1er champ ajouté"), blank=True, max_length=255, null=True)
    address = models.CharField(_("Adresse"), blank=False, max_length=510, null=False)
    annual_income = models.DecimalField(
        _("Revenus annuels ($)"), blank=True, decimal_places=0, max_digits=9, null=True
    )
    apartments_number = models.PositiveIntegerField(_("Nombre d'appartements"), blank=True, null=True)
    bathrooms_number = models.CharField(
        _("Nombre de salles de bain"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.BATHROOMS_NUMBER),
        default='',
        max_length=10
    )
    bedrooms_number = models.CharField(
        _("Nombre de chambres"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.BEDROOMS_NUMBER),
        default='',
        max_length=10
    )
    building_type = models.CharField(
        _("Type de bâtiment"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.BUILDINGS_TYPES),
        default='',
        max_length=50
    )
    ccd = models.DecimalField(
        _("Ccd (CCD)"), blank=True, decimal_places=2, max_digits=5, null=True
    )
    city = models.CharField(
        _("Ville"),
        blank=False,
        choices=choices_format_to_tuple(static_variables.CANADIAN_CITIES),
        default='montreal',
        max_length=100,
        null=False
    )
    construction_age = models.CharField(
        _("L'âge du construction"),
        blank=True,
        choices=choices_format_to_tuple(static_variables.CONSTRUCTION_AGE),
        default='',
        max_length=50
    )
    cost_per_housing = models.DecimalField(
        _("Coût par logement (CPL) ($)"), blank=True, decimal_places=0, max_digits=9, null=True
    )
    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    description = models.TextField(_("Description"), blank=False, null=False)
    down_payment_required = models.DecimalField(
        _("Mise de fond minimal ($)"), blank=True, decimal_places=0, max_digits=9, null=True
    )
    economic_value = models.DecimalField(
        _("Valeur économique ($)"), blank=True, decimal_places=0, max_digits=9, null=True
    )
    gps_latitude = models.FloatField(_("Latitude"), blank=True, default=46.813878, null=True)
    gps_longitude = models.FloatField(_("Longitude"), blank=True, default=-71.207981, null=True)
    gross_revenue_multiplier = models.DecimalField(
        _("Multiplicateur de revenu brut (MRB)"), blank=True, decimal_places=1, max_digits=4, null=True
    )
    has_dining_room = models.BooleanField(_("Salle à manger"), default=False)
    has_fireplace = models.BooleanField(_("Cheminée"), default=False)
    has_garage = models.BooleanField(_("Garage"), default=False)
    has_garden = models.BooleanField(_("Jardin"), default=False)
    has_swimming_pool = models.BooleanField(_("Piscine"), default=False)
    housing_descriptions = models.CharField(_("Description des logements"), blank=True, max_length=1020, null=True)
    image_map = models.ImageField(
        help_text=_("L'image de la carte de la propriété."),
        null=True, blank=True,
        upload_to=settings.IMAGES_FOLDER + 'item/itemsImages'  # lien de l'image: /media/item/images/itemsImages/*.*
    )
    item_id = models.CharField(_("Id"), max_length=255, primary_key=True, unique=True)
    is_active = models.BooleanField(_("Est active"), default=True)
    label = models.CharField(_("Étiquette"), blank=False, max_length=255, null=False)
    lot_size = models.PositiveIntegerField(_("Taille de la propriété(m²)"), default=0)
    maximum_loan = models.DecimalField(
        _("Prêt maximal (%)"), blank=True, decimal_places=2, max_digits=5, null=True
    )
    net_income_multiplier = models.DecimalField(
        _("Multiplicateur de revenu net (MRN)"), blank=True, decimal_places=1, max_digits=4, null=True
    )
    overall_rate_update = models.DecimalField(
        _("Taux global d'actualisation (TGA) (%)"), blank=True, decimal_places=1, max_digits=4, null=True
    )
    price = models.DecimalField(
        _("Prix"), blank=False, decimal_places=0, default=0, max_digits=9, null=False
    )
    property_type = models.CharField(
        _("Type de la Propriété"),
        blank=False,
        choices=choices_format_to_tuple(static_variables.PROPERTIES_TYPES),
        default='',
        max_length=50,
        null=False
    )
    short_description = models.CharField(_("Brèf description"), max_length=255, null=False, blank=False)
    status = models.CharField(
        _("Statut"),
        choices=choices_format_to_tuple(static_variables.ITEMS_STATUS),
        default='for_sale',
        max_length=50
    )
    with_map = models.BooleanField(_("Avec Carte"), default=False)

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
        help_text=_("Image de l'article."),
        upload_to=settings.IMAGES_FOLDER + 'item/itemsImages'  # lien de l'image: /media/item/images/itemsImages/*.*
    )
    item = models.ForeignKey(
        Item,
        db_index=True,
        help_text=_("L'article."),
        on_delete=models.CASCADE,
        related_name="images"
    )

    def __str__(self):
        return str(self.image)[str(self.image).rfind('/') + 1:]

    @property
    def image_filename(self):
        return os.path.basename(self.image.name)
