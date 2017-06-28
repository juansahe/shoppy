# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-28 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('img', models.ImageField(upload_to='uploads/category/', verbose_name='Imagen')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre del producto ')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripci\xf3n del producto ')),
                ('img', models.ImageField(upload_to='uploads/products/', verbose_name='Imagen del producto ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='Categoria')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider', verbose_name='Marca o Retail')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]