# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-17 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
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
        migrations.AlterField(
            model_name='funding',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
    ]