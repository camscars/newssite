# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20160519_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]