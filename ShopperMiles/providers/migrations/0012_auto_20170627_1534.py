# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-27 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0011_auto_20170627_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bond',
            name='value',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='value_bond1',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='value_bond2',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='value_bond3',
        ),
        migrations.AddField(
            model_name='bond',
            name='value1',
            field=models.CharField(default=1, max_length=200, verbose_name='Valor 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='value2',
            field=models.CharField(default=1, max_length=200, verbose_name='Valor 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='value3',
            field=models.CharField(default=1, max_length=200, verbose_name='Valor 3'),
            preserve_default=False,
        ),
    ]
