# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_backend', '0003_auto_20170726_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='maxVal',
            field=models.FloatField(default=0),
        ),
    ]