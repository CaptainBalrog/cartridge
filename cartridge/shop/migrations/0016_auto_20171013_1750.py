# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-13 17:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20171009_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='arriving',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='departing',
        ),
    ]
