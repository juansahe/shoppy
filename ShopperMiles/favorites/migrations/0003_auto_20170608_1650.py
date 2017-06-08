# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-08 21:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0002_auto_20170608_1615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['pk'], 'verbose_name': 'Favorito', 'verbose_name_plural': 'Favoritos'},
        ),
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
