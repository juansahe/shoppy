# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-08 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170607_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
            preserve_default=False,
        ),
    ]
