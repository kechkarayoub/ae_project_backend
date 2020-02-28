# -*- coding: utf-8 -*-

from.models import Leasing
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


def on_transaction_commit(func):
    def inner(*args, **kwargs):
        transaction.on_commit(lambda: func(*args, **kwargs))

    return inner


@receiver(post_save, sender=Leasing)
@on_transaction_commit
def create_next_leasing_entry(sender, **kwargs):
    created_leasing = kwargs['instance']
    today = datetime.datetime.today()
    if today.day >= 28 and created_leasing.createdBy == "admin":
        try:
            next_month_treated = today.replace(month=today.month + 1)
        except ValueError:
            if today.month == 12:
                next_month_treated = today.replace(year=today.year + 1, month=1)
            else:
                next_month_treated = today.replace(month=today.month + 1, day=1)
        if not Leasing.objects.filter(
            client=created_leasing.client,
            item=created_leasing.item,
            month_treated=format(next_month_treated, '%m/%Y')
        ).exists():
            Leasing.objects.create(
                client=created_leasing.client,
                createdBy="automatically",
                end_at=created_leasing.end_at,
                item=created_leasing.item,
                month_treated=format(next_month_treated, '%m/%Y'),
                payment_day=created_leasing.payment_day,
                price=created_leasing.price,
                start_at=created_leasing.start_at
            )