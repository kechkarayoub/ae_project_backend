# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-17 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0003_auto_20191117_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='funding',
            name='description_fr',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
    ]
