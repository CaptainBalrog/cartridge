# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-09 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20170821_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='arriving',
            field=models.DateField(default='2017-09-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='departing',
            field=models.DateField(default='2017-09-13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariation',
            name='arriving',
            field=models.DateField(default='2017-09-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariation',
            name='departing',
            field=models.DateField(default='2017-09-13'),
            preserve_default=False,
        ),
    ]
