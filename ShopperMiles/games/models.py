# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models

from products.models import Product

class Level(models.Model):
    # additional fields here
    number = models.IntegerField(verbose_name="Numero de nivel ")
    point_xp = models.IntegerField(verbose_name="Experiencia del nivel ")
    point_sm = models.IntegerField(verbose_name="Puntos SM para este nivel ")
    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "Nivel"
        verbose_name_plural = "Niveles"
        ordering = ['number']


class Task(models.Model):
    # additional fields here
    level = (
    ('bro', 'Bronce'),
    ('pla', 'Plata'),
    ('oro', 'Oro'),
    ('platinum', 'Platinum'),
)

    task = (
    ('pre', 'Pregunta rapida'),
    ('mir', 'Mira esta imagen'),
    ('subir', 'Subir factura'),
)

    name =  models.CharField( verbose_name="Titulo de la  tarea",max_length=255,choices=task,default='pre', help_text="Nombre de la tarea")
    #pregunta rapida
    pregunta = models.CharField(verbose_name="Pregunta rapida",max_length=255,null=True, blank=True,help_text="Llenar si la tarea es de pregunta rapida")
    respuesta = models.CharField(verbose_name="Respuesta",max_length=255,null=True, blank=True,help_text="Llenar si la tarea es de pregunta rapida")
    #Mira una imagen

    imagen = models.ImageField(verbose_name="Tarea de ver imagen",
                            upload_to='uploads/task/ver_img',blank=True,help_text="Llenar si la tarea es ver imagen")

    #Sube factura
    
    factura = models.CharField(verbose_name="Factura",max_length=255,null=True, blank=True,help_text="Llenar si la tarea es subir una factura")
    imagen_factura = models.ImageField(verbose_name="Imagen",
                            upload_to='uploads/task/img_factu',null=True,blank=True,help_text="Llenar si la tarea es subir una factura")


    type_task =  models.CharField( verbose_name=" Tipo de tarea",max_length=20,choices=level,default='bro',)
    point_exp = models.IntegerField(verbose_name="Experiencia de la tarea")
    SM = models.IntegerField(verbose_name="Puntos SM de esta tarea")
    level = models.ForeignKey(Level, verbose_name="Nivel", on_delete=models.CASCADE,)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        primary_key=False,
        verbose_name="Producto"
    )

    def __str__(self):
        return self.type_task

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['pk']

