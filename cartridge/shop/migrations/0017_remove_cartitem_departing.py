# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-13 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20171013_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='departing',
        ),
    ]
