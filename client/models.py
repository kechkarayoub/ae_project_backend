# -*- coding: utf-8 -*-
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext as _
from item.models import Item
import datetime

TYPES = (
    ("buyer", _("Achteur")),
    ("seller", _("Vendeur")),
    ("tenant", _("Locataire"))
)


YEARMONTH_INPUT_FORMATS = (
    '%m-%Y', '%m/%Y', # '2006-10', '10/2006'
)


class Client(models.Model):
    class Meta:
        db_table = "client"

    createdAt = models.DateTimeField(_("Créé le"), auto_now_add=True)
    email = models.EmailField(_("Email"), null=True)
    first_name = models.CharField(_("Prénom"), blank=False, max_length=30)
    is_active = models.BooleanField(_("Est active"), default=True)
    last_name = models.CharField(_("Nom"), blank=False, max_length=30)
    phone = models.CharField(_("Téléphone"), blank=True, default="", max_length=20)
    type = models.CharField(_("Type"), blank=False, choices=TYPES, default="tenant", max_length=20)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.full_name()


class YearMonthField(models.CharField):
    default_error_messages = {
        'invalid': _('Enter a valid year and month.'),
    }

    def __init__(self, input_formats=None, *args, **kwargs):
        super(YearMonthField, self).__init__(*args, **kwargs)
        self.input_formats = input_formats

    def clean(self, value, hh):
        if value in validators.EMPTY_VALUES:
            return None
        if isinstance(value, datetime.datetime):
            return format(value, '%m/%Y')
        if isinstance(value, datetime.date):
            return format(value, '%m/%Y')
        for fmt in self.input_formats or YEARMONTH_INPUT_FORMATS:
            try:
                date = datetime.datetime.strptime(value, fmt)
                return format(date, '%m/%Y')
            except ValueError:
                continue
        raise ValidationError(self.error_messages['invalid'])


class Leasing(models.Model):
    class Meta:
        db_table = "leasing"
        unique_together = ['client', 'item', 'month_treated']

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="rented_items_by_months")
    createdAt = models.DateTimeField(_("Créé le"), auto_now_add=True)
    createdBy = models.CharField(_("Créé par"), blank=False, default="celery", max_length=30)
    end_at = models.DateTimeField(_("Fin à"), null=True)
    is_active = models.BooleanField(_("Est active"), default=True)
    is_paid = models.BooleanField(_("Est payé"), default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="tenants_by_months")
    month_treated = YearMonthField(
        default=format(datetime.datetime.now(), '%m/%Y'), help_text="mm/aaaa ou mm-aaaa", max_length=10
    )
    payment_day = models.PositiveIntegerField(
        _("Jour de paiement"), default=28, validators=[MaxValueValidator(31), MinValueValidator(1)]
    )
    price = models.DecimalField(
        _("Prix"), blank=False, decimal_places=0, default=0, max_digits=9, null=False
    )
    start_at = models.DateTimeField(_("Commencer à"), default=datetime.datetime.now)

    def __str__(self):
        return self.client.full_name() + "-" + self.item.label + "-" + str(self.month_treated)
