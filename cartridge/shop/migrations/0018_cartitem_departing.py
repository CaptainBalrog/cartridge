# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-13 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_remove_cartitem_departing'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='departing',
            field=models.DateField(default='2017-10-13'),
            preserve_default=False,
        ),
    ]
