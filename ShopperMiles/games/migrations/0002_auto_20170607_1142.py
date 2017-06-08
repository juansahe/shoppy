# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-07 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='level',
            options={'ordering': ['number'], 'verbose_name': 'Nivel', 'verbose_name_plural': 'Niveles'},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['pk'], 'verbose_name': 'Tarea', 'verbose_name_plural': 'Tareas'},
        ),
        migrations.RemoveField(
            model_name='level',
            name='point',
        ),
        migrations.AddField(
            model_name='level',
            name='point_sm',
            field=models.IntegerField(default=1, verbose_name='Puntos SM para este nivel '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='level',
            name='point_xp',
            field=models.IntegerField(default=1, verbose_name='Experiencia del nivel '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='level',
            name='number',
            field=models.IntegerField(verbose_name='Numero de nivel '),
        ),
        migrations.AlterField(
            model_name='task',
            name='SM',
            field=models.IntegerField(verbose_name='Puntos SM de esta tarea'),
        ),
        migrations.AlterField(
            model_name='task',
            name='point_exp',
            field=models.IntegerField(verbose_name='Experiencia de la tarea'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type_task',
            field=models.CharField(choices=[('bro', 'Bronce'), ('pla', 'Plata'), ('oro', 'Oro')], default='bro', max_length=20, verbose_name=' Tipo de tarea'),
        ),
    ]