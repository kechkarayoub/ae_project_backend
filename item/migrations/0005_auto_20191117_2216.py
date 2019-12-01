# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-17 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_auto_20191117_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='annual_income',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=9, null=True, verbose_name='Annual incomes ($)'),
        ),
        migrations.AlterField(
            model_name='item',
            name='lot_size',
            field=models.PositiveIntegerField(default=0, verbose_name='Property size(m²)'),
        ),
    ]