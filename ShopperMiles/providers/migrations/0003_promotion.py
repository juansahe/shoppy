# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-07 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_auto_20170607_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.TextField(null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Promoción',
                'verbose_name_plural': 'Promociones',
                'ordering': ['name'],
            },
        ),
    ]
