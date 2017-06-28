# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-28 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Numero de nivel ')),
                ('point_xp', models.IntegerField(verbose_name='Experiencia del nivel ')),
                ('point_sm', models.IntegerField(verbose_name='Puntos SM para este nivel ')),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': 'Nivel',
                'verbose_name_plural': 'Niveles',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('pre', 'Pregunta rapida'), ('mir', 'Mira esta imagen'), ('subir', 'Subir factura')], default='pre', help_text='Nombre de la tarea', max_length=255, verbose_name='Titulo de la  tarea')),
                ('pregunta', models.CharField(blank=True, help_text='Llenar si la tarea es de pregunta rapida', max_length=255, null=True, verbose_name='Pregunta rapida')),
                ('respuesta', models.CharField(blank=True, help_text='Llenar si la tarea es de pregunta rapida', max_length=255, null=True, verbose_name='Respuesta')),
                ('imagen', models.ImageField(blank=True, help_text='Llenar si la tarea es ver imagen', upload_to='uploads/task/ver_img', verbose_name='Tarea de ver imagen')),
                ('factura', models.CharField(blank=True, help_text='Llenar si la tarea es subir una factura', max_length=255, null=True, verbose_name='Factura')),
                ('imagen_factura', models.ImageField(blank=True, help_text='Llenar si la tarea es subir una factura', null=True, upload_to='uploads/task/img_factu', verbose_name='Imagen')),
                ('type_task', models.CharField(choices=[('bro', 'Bronce'), ('pla', 'Plata'), ('oro', 'Oro'), ('platinum', 'Platinum')], default='bro', max_length=20, verbose_name=' Tipo de tarea')),
                ('point_exp', models.IntegerField(verbose_name='Experiencia de la tarea')),
                ('SM', models.IntegerField(verbose_name='Puntos SM de esta tarea')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Level', verbose_name='Nivel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Producto')),
            ],
            options={
                'ordering': ['pk'],
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
        ),
    ]