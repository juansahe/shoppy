# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-08 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170608_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(default='1', max_length=100, null=True),
        ),
    ]
