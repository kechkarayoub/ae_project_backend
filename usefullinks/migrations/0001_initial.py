# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-11 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinkCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=510, verbose_name='Label')),
                ('label_en', models.CharField(max_length=510, null=True, verbose_name='Label')),
                ('label_fr', models.CharField(max_length=510, null=True, verbose_name='Label')),
            ],
            options={
                'db_table': 'link_category',
            },
        ),
        migrations.CreateModel(
            name='UsefulLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=510, verbose_name='Label')),
                ('label_en', models.CharField(max_length=510, null=True, verbose_name='Label')),
                ('label_fr', models.CharField(max_length=510, null=True, verbose_name='Label')),
                ('url', models.CharField(max_length=510, verbose_name='Url')),
                ('category', models.ForeignKey(help_text="Link's category", on_delete=django.db.models.deletion.CASCADE, related_name='links', to='usefullinks.LinkCategory')),
            ],
            options={
                'db_table': 'useful_link',
            },
        ),
    ]