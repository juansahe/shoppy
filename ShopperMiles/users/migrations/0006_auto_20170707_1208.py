# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-07 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170707_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.Level'),
        ),
    ]
