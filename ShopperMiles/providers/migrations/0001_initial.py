# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-28 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripci\xf3n')),
                ('value1', models.CharField(max_length=200, verbose_name='Valor 1')),
                ('value2', models.CharField(max_length=200, verbose_name='Valor 2')),
                ('value3', models.CharField(max_length=200, verbose_name='Valor 3')),
                ('code', models.CharField(max_length=200, verbose_name='Codigo')),
                ('status', models.CharField(choices=[('0', 'Activo'), ('1', 'Redimido')], default='0', max_length=200, verbose_name='Estado')),
                ('img', models.ImageField(null=True, upload_to='uploads/bond/', verbose_name='Imagen')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Bono',
                'verbose_name_plural': 'Bonos',
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripci\xf3n')),
                ('img', models.ImageField(null=True, upload_to='uploads/promotion/', verbose_name='Imagen')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Promoci\xf3n',
                'verbose_name_plural': 'Promociones',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_provider', models.CharField(choices=[('0', 'Marca'), ('1', 'Retail')], default='0', max_length=200, verbose_name='Tipo')),
                ('web_site', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sitio web')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('description', models.TextField(null=True, verbose_name='Descripci\xf3n')),
                ('phone_contact', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono contacto')),
                ('name_contact', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre contacto')),
                ('email_contact', models.CharField(blank=True, max_length=200, null=True, verbose_name='Email contacto')),
                ('img', models.ImageField(upload_to='uploads/marks/', verbose_name='Logo')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.AddField(
            model_name='promotion',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider', verbose_name='Marca o Retail'),
        ),
        migrations.AddField(
            model_name='bond',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.Provider', verbose_name='Marca o Retail'),
        ),
    ]
