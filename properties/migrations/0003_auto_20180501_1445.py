# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-01 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20180501_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='zip_code',
            field=models.IntegerField(null=True),
        ),
    ]