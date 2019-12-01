# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-17 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_db', '0005_auto_20191117_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsdb',
            name='header_image',
            field=models.ImageField(help_text='Header image', null=True, upload_to='images/settings_db/header'),
        ),
        migrations.AlterField(
            model_name='settingsdb',
            name='logo',
            field=models.ImageField(help_text='Logo image', null=True, upload_to='images/settings_db/header'),
        ),
        migrations.AlterField(
            model_name='settingsdb',
            name='main_bg_image',
            field=models.ImageField(help_text='Body background image', null=True, upload_to='images/settings_db/header'),
        ),
    ]