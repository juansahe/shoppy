# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-05 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(choices=[('Pregunta rapida', 'Pregunta rapida'), ('Mira esta imagen', 'Mira esta imagen'), ('Subir factura', 'Subir factura')], default='pre', help_text='Nombre de la tarea', max_length=255, verbose_name='Titulo de la  tarea'),
        ),
    ]
