# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models

class Product(models.Model):
    # additional fields here
    name = models.CharField(verbose_name="Nombre del producto ",max_length=200)
    description = models.TextField( verbose_name="Descripción del producto ",null=True,blank=True)
    img = models.ImageField(verbose_name="Imagen del producto ",upload_to = 'uploads/products/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

class Category(models.Model):
    # additional fields here
    name = models.CharField( verbose_name="Nombre",max_length=200)
    img = models.ImageField( verbose_name="Imagen",upload_to = 'uploads/category/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']
