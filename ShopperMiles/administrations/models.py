# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models


class Mensaje(models.Model):
    name = models.CharField(verbose_name = "Nombre",max_length=255)
    mensaje = models.CharField( verbose_name = "Mensaje",max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mensaje de la aplicación"
        verbose_name_plural = "Mensajes de la aplicación"
        ordering = ['pk']
