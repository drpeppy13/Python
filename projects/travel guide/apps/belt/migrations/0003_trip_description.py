# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-25 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0002_auto_20180625_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
